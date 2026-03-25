import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong2/latlong.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Material App',
      home: locationScreen(),
    );
  }
}


class locationScreen extends StatefulWidget {
  const locationScreen({super.key});

  @override
  State<locationScreen> createState() => _locationScreenState();
}

class _locationScreenState extends State<locationScreen> {
  //String latitud = "No disponible";
  //String longituf = "No disponible";

  LatLng _currentPosition = LatLng(19.4326, -99.1332);

  final MapController _mapController = MapController();

  Future<void> obtenerUbicacion() async {
    bool servicioHabilitado;
    LocationPermission permiso;


    servicioHabilitado = await Geolocator.isLocationServiceEnabled();
    if (!servicioHabilitado) {
      return;
    }

    permiso = await Geolocator.checkPermission();
    if (permiso == LocationPermission.denied) {
      permiso = await Geolocator.requestPermission();
      if (permiso == LocationPermission.denied) {
        return;
      }
    }

    if(permiso == LocationPermission.deniedForever){
      return;
    }

    Position posicion = await Geolocator.getCurrentPosition(
      desiredAccuracy: LocationAccuracy.high
    );

    setState(() {
      _currentPosition = LatLng(posicion.latitude, posicion.longitude);
      _mapController.move(_currentPosition, 15.0);
    });

  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Ubiubi nomi'),
      ),
      
      body: FlutterMap(
        mapController: _mapController,
        options: MapOptions(
          center: _currentPosition, 
          zoom: 14.0,
        ),
        
        children: [
          TileLayer(
            urlTemplate: "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
            userAgentPackageName: "com.victus.ubiubi_nomi", 
          ),
          MarkerLayer(
            markers: [
              Marker(
                point: _currentPosition,
                width: 80.0,
                height: 80.0,
                child: const Icon(
                  Icons.location_on,
                  color: Colors.red,
                  size: 40,
                ),
              ),
            ],
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: obtenerUbicacion,
        child: const Icon(Icons.my_location),
      ),
    );
  }
}