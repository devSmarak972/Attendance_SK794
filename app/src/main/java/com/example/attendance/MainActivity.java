package com.example.attendance;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.view.View;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @RequiresApi(api = Build.VERSION_CODES.S)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void openLogin(View v){
        Intent intent = new Intent(this, Login.class);
        startActivity(intent);
    }
    public void openSignup(View v){
        Intent intent = new Intent(this, SignUp.class);
        startActivity(intent);
    }
}