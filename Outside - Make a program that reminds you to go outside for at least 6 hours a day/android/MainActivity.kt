package com.example.gooutsidereminder

import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.os.Build
import android.os.Handler
import android.os.Looper
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.NotificationCompat
import android.os.Bundle

class MainActivity : AppCompatActivity() {

    private var totalHours = 0
    private val targetHours = 6
    private val handler = Handler(Looper.getMainLooper())
    private lateinit var progressText: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        progressText = findViewById(R.id.progressText)
        val startTrackingButton: Button = findViewById(R.id.startTrackingButton)

        createNotificationChannel()

        startTrackingButton.setOnClickListener {
            startTracking()
        }
    }

    private fun startTracking() {
        handler.postDelayed(object : Runnable {
            override fun run() {
                if (totalHours < targetHours) {
                    totalHours++
                    sendNotification("Go Outside Reminder", "Time to go outside! Total: $totalHours hour(s)")
                    progressText.text = "Time spent outside: $totalHours hours"
                    handler.postDelayed(this, 3600000) // 1 hour in milliseconds
                } else {
                    sendNotification("Congrats!", "You've spent 6 hours outside today!")
                }
            }
        }, 0)
    }

    private fun sendNotification(title: String, message: String) {
        val intent = Intent(this, MainActivity::class.java)
        val pendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE)

        val notification = NotificationCompat.Builder(this, "GO_OUTSIDE_CHANNEL")
            .setContentTitle(title)
            .setContentText(message)
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setContentIntent(pendingIntent)
            .setAutoCancel(true)
            .build()

        val notificationManager = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        notificationManager.notify(totalHours, notification)
    }

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                "GO_OUTSIDE_CHANNEL",
                "Go Outside Reminders",
                NotificationManager.IMPORTANCE_DEFAULT
            )
            val manager = getSystemService(NotificationManager::class.java)
            manager.createNotificationChannel(channel)
        }
    }
}