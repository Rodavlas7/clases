import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
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
  String latitud = "No disponible";
  String longituf = "No disponible";

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
      latitud = posicion.latitude.toString();
      longituf = posicion.longitude.toString();
    });

  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Ubiubi nomi'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("Latitud: $latitud"),
            Text("Longitud: $longituf"),
            ElevatedButton(
              onPressed: obtenerUbicacion, 
              child: const Text("Obtener Ubicación")
            )
          ],
        ),
      ), 
    );
  }
}