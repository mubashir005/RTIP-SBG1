package com.example.blind_guider_app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;

public class First_Screen extends AppCompatActivity {
    private static int SPLASH_TIME_OUT = 5000;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_first__screen);

        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {

                Intent homeintent = new Intent(First_Screen.this ,Second_Screen.class);
                startActivity(homeintent);
                finish();
            }
        },SPLASH_TIME_OUT);
    }
}