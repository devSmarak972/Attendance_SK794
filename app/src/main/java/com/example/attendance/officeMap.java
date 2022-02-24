package com.example.attendance;

import android.content.Intent;
import android.os.Bundle;
import android.widget.SearchView;
import android.widget.Toast;

import androidx.fragment.app.FragmentActivity;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.libraries.places.api.Places;
import com.google.android.libraries.places.api.model.Place;
import com.google.android.libraries.places.api.net.PlacesClient;
import com.google.android.libraries.places.widget.Autocomplete;
import com.google.android.libraries.places.widget.model.AutocompleteActivityMode;

import java.util.Arrays;
import java.util.List;

import io.reactivex.annotations.NonNull;
import io.reactivex.annotations.Nullable;

public class officeMap extends FragmentActivity implements OnMapReadyCallback {

    SearchView searchView;
    SupportMapFragment eventMapFragment;
    double latitude;
    double longitude;
    LatLng latLng;
    private List<Place.Field> fields;
    final int request = 1;
    String name;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_office_map);
        searchView = findViewById(R.id.search);
        eventMapFragment = (SupportMapFragment)  getSupportFragmentManager().findFragmentById(R.id.map1);
        assert eventMapFragment != null;
        fields = Arrays.asList(Place.Field.ID, Place.Field.NAME, Place.Field.LAT_LNG);
        Places.initialize(getApplicationContext(),"AIzaSyCU5z8oAnm8dAJyaVo6pdT35jEMu-FqRmY");
        PlacesClient placesClient = Places.createClient(this);
        Intent intent = new Autocomplete.IntentBuilder(AutocompleteActivityMode.FULLSCREEN,fields).build(officeMap.this);
//        Toast.makeText(this, "Starting intent", Toast.LENGTH_SHORT).show();
        startActivity(intent);
    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        Toast.makeText(this, "Starting intent", Toast.LENGTH_SHORT).show();
        super.onActivityResult(requestCode, resultCode, data);
        switch (resultCode){
            case request:
                Place place = Autocomplete.getPlaceFromIntent(data);
                name = place.getName();
                latLng = place.getLatLng();
                eventMapFragment.getMapAsync(officeMap.this);
                break;
        }
    }
    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera.
     * In this case, we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to
     * install it inside the SupportMapFragment. This method will only be triggered once the
     * user has installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(@NonNull GoogleMap googleMap) {
        googleMap.addMarker(new MarkerOptions().position(latLng).title("Office Location"));
        googleMap.animateCamera(CameraUpdateFactory.newLatLngZoom(latLng,10.0f));
    }
}