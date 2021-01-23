package com.example.blind_guider_app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;

public class Third_Screen extends AppCompatActivity {

    Button buttonid;
    Intent intent;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_third__screen);
        buttonid=findViewById(R.id.buttonid);


        //ye cheze aik page se dusre pe le kr jati h
        buttonid.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try
                {
                    Intent intent = new Intent();
                    intent.setAction(MediaStore.ACTION_IMAGE_CAPTURE);
                    startActivity(intent);
                }
                catch (Exception e) {
                    e.printStackTrace();

                }
            }
        });


        }
    }
