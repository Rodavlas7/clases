import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong2/latlong.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Localizacion(),
    );
  }
}

class Localizacion extends StatefulWidget {
  const Localizacion({super.key});

  @override
  State<Localizacion> createState() => _LocalizacionState();
}

class _LocalizacionState extends State<Localizacion> {
  LatLng _posicionActual = const LatLng(0, 0);
  final MapController _mapController = MapController();

  @override
  void initState() {
    super.initState();
    obtenerUbicacion();
  }

  Future<void> obtenerUbicacion() async {
    bool servicioHabilitado = await Geolocator.isLocationServiceEnabled();
    if (!servicioHabilitado) return;

    LocationPermission permiso = await Geolocator.checkPermission();

    if (permiso == LocationPermission.denied) {
      permiso = await Geolocator.requestPermission();
      if (permiso == LocationPermission.denied) return;
    }

    if (permiso == LocationPermission.deniedForever) return;

    Position posicion = await Geolocator.getCurrentPosition(
      desiredAccuracy: LocationAccuracy.high,
    );

    final nuevaPosicion = LatLng(posicion.latitude, posicion.longitude);

    setState(() {
      _posicionActual = nuevaPosicion;
    });

    _mapController.move(nuevaPosicion, 15.0);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Ruta Segura'),
      ),
      body: Column(
        children: [
          Expanded(
            child: FlutterMap(
              mapController: _mapController,
              options: MapOptions(
                initialCenter: _posicionActual,
                initialZoom: 15.0,
              ),
              children: [
                TileLayer(
                  urlTemplate: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
                  userAgentPackageName: 'com.RutaSegura.app',
                ),
                MarkerLayer(
                  markers: [
                    Marker(
                      point: _posicionActual,
                      width: 80,
                      height: 80,
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
          ),
          Padding(
            padding: const EdgeInsets.all(10),
            child: Text(
              'Lat: ${_posicionActual.latitude}, Lng: ${_posicionActual.longitude}',
            ),
          ),
          ElevatedButton(
            onPressed: obtenerUbicacion,
            child: const Text('Actualizar ubicación'),
          ),
        ],
      ),
    );
  }
}