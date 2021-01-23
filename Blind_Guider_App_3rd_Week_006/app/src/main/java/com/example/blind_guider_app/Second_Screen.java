package com.example.blind_guider_app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;

public class Second_Screen extends AppCompatActivity {
    Button nextid;
    Intent intent;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second__screen);
        nextid=findViewById(R.id.nextid);
        nextid.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent=new Intent(Second_Screen.this, Third_Screen.class);
                startActivity(intent);
            }
        });

    }
}