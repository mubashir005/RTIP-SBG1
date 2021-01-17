package com.example.firstweek;

import androidx.appcompat.app.AppCompatActivity;


import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.os.Bundle;

import android.speech.RecognizerIntent;
import android.view.Menu;
import android.view.View;
import android.widget.ImageButton;
import android.provider.MediaStore;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Locale;

public class Urdulang extends AppCompatActivity {

    Button camera;
    private ImageButton Speak;
    private final int REQ_CODE_SPEECH_INPUT = 1001;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_urdulang);

        TextView txtSpeechInput = (TextView) findViewById(R.id.txtSpeechInput);
        Speak = (ImageButton) findViewById(R.id.Speak3);

        // hide the action bar
        /* getActionBar().hide();*/

        Speak.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                promptSpeechInput();
            }
        });

    }

    /**
     * Showing google speech input dialog
     * */
    private void promptSpeechInput() {
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, "ur-rPK");
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        intent.putExtra(RecognizerIntent.EXTRA_PROMPT, getString(R.string.speech_prompt));
        try {
            startActivityForResult(intent, REQ_CODE_SPEECH_INPUT);
        } catch (ActivityNotFoundException a) { Toast.makeText(getApplicationContext(),getString(R.string.speech_not_supported),Toast.LENGTH_SHORT).show();
        }
    }

    /**
     * Receiving speech input and Moving to requested activity
     * */
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data){
        if (requestCode == REQ_CODE_SPEECH_INPUT){
            if (resultCode == RESULT_OK){
                ArrayList<String> result = data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);

                if (result.size() == 0) {
                    // didn't hear anything
                } else {
                    String userinput = result.get(0);
                    // toUpperCase() used to make string comparison equal
                    if(userinput.toUpperCase().equals("رہنمائی")){

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

                    else if(userinput.toUpperCase().equals("رائے")) {
                        startActivity(new Intent(this, Feedback.class));
                    }
                    else if(userinput.toUpperCase().equals("روانگی")) {
                        finish();
                        System.exit(0);

                    }

                }
            }
            else if (resultCode==RecognizerIntent.RESULT_AUDIO_ERROR){
                showToastMessage("Audio Error");
            }
            else if((resultCode==RecognizerIntent.RESULT_CLIENT_ERROR)){
                showToastMessage("Client Error");

            }
            else if(resultCode==RecognizerIntent.RESULT_NETWORK_ERROR){
                showToastMessage("Network Error");
            }
            else if (resultCode==RecognizerIntent.RESULT_NO_MATCH){
                showToastMessage("No Match");
            }
            else if(resultCode==RecognizerIntent.RESULT_SERVER_ERROR){
                showToastMessage("Server Error");
            }
        }

        super.onActivityResult(requestCode, resultCode, data);
    }
    void showToastMessage(String message){
        Toast.makeText(this,message,Toast.LENGTH_LONG).show();
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    public void obsdet(View view) {

        startActivity(new Intent(this, strtObstackleDetection.class));
    }

    public void fed(View view) {
        startActivity(new Intent(this, Feedback.class));
    }

    public void exit(View view) {
        finish();
        System.exit(0);
    }
}
