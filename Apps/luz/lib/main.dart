import 'dart:async';
import 'package:ambient_light/ambient_light.dart';
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Medidor de Luz',
      theme: ThemeData(primarySwatch: Colors.blueGrey),
      debugShowCheckedModeBanner: false,
      home: const LightScreen(),
    );
  }
}

class LightScreen extends StatefulWidget {
  const LightScreen({super.key});

  @override
  _LightScreenState createState() => _LightScreenState();
}

class _LightScreenState extends State<LightScreen> {
  double _lightLevel = 0.0;
  String mensaje = 'Iniciando...';
  final AmbientLight _ambientLight = AmbientLight();
  StreamSubscription<double>? _lightSubscription;

  @override
  void initState() {
    super.initState();
    _iniciarSensorLuz();
  }

  void _iniciarSensorLuz() {
    _lightSubscription = _ambientLight.ambientLightStream.listen((double lux) {
      setState(() {
        _lightLevel = lux;
        if (_lightLevel < 10) {
          mensaje = 'Muy oscuro';
        } else if (_lightLevel < 100) {
          mensaje = 'Luz normal';
        } else if (_lightLevel < 1000) {
          mensaje = 'Está brillante';
        } else {
          mensaje = 'Mucha luz';
        }
      });
    });
  }

  @override
  void dispose() {
    _lightSubscription?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    Color fondo = Colors.white;
    Color texto = Colors.black;

    if (_lightLevel < 10) {
      fondo = Colors.grey[900]!; 
      texto = Colors.white;
    } else if (_lightLevel < 100) {
      fondo = Colors.grey[200]!;
      texto = Colors.black;
    } else if (_lightLevel < 1000) {
      fondo = Colors.amber[100]!;
      texto = Colors.black87;
    } else {
      fondo = Colors.amber[400]!;
      texto = Colors.black;
    } 

    return Scaffold(
      backgroundColor: fondo,
      appBar: AppBar(
        title: const Text('Sensor de Luz'),
        backgroundColor: Colors.blueGrey[900],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              width: 200,
              height: 200,
              decoration: BoxDecoration(
                color: _lightLevel < 10 ? Colors.grey[800] : Colors.amber[100],
                shape: BoxShape.circle,
                border: Border.all(color: Colors.amber, width: 4
                ),
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    _lightLevel.toStringAsFixed(2),
                    style: TextStyle(
                      fontSize: 24, 
                      color: texto, 
                      fontWeight: FontWeight.bold
                    ),
                  ),
                  const SizedBox(height: 10),
                  Text(
                    'Lux',
                    style: TextStyle(
                      fontSize: 18,
                      color: texto.withOpacity(0.7)
                      ),
                  ),
                ],
              )
            ),
            const SizedBox(height: 30),

            Container(
              padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 15),
              decoration: BoxDecoration(
                color: _lightLevel < 50 ? Colors.grey[800] : Colors.white,
                borderRadius: BorderRadius.circular(30),
                boxShadow: const [
                  BoxShadow(
                    color: Colors.black26,
                    blurRadius: 10,
                    offset: Offset(0, 4),
                  ),
                ],
              ),
              child: Text(
                mensaje,
                style: TextStyle(
                  fontSize: 22,
                  color: texto,
                  fontWeight: FontWeight.w500
                ),
              ),
            ),
            const SizedBox(height: 30),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 40),
              child: Column( 
                children: [
                  Text(
                    'Intensidad de Luz',
                    style: TextStyle(
                      fontSize: 18,
                      color: texto,
                    ),
                  ),
                  const SizedBox(height: 10),
                  LinearProgressIndicator(
                    value: (_lightLevel/1000).clamp(0.0, 1.0),
                    backgroundColor: Colors.grey[300],
                    valueColor: AlwaysStoppedAnimation<Color>(
                      _lightLevel > 500 ? Colors.amber : Colors.grey!,
                    ),
                    minHeight: 15,
                  )
                ],

              )
            ),
            const SizedBox(height: 40),
            Text(
              'Tapa el sensor o acerca una fuente de luz para ver los cambios',
              style: TextStyle(
                fontSize: 14,
                color: texto.withOpacity(0.7),
              ),
            ),
          ],
        ),
      ),
    );
  }
}