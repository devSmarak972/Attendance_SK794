package com.example.attendance;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void openLogin(View v){
//        Toast.makeText(this, "Landing on Login page", Toast.LENGTH_SHORT).show();
        Intent intent = new Intent(this, Login.class);
        startActivity(intent);
    }
    public void openSignup(View v){
//        Toast.makeText(this, "Landing on Login page", Toast.LENGTH_SHORT).show();
        Intent intent = new Intent(this, SignUp.class);
        startActivity(intent);
    }
}