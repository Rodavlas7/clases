import 'package:flutter/material.dart';
import 'package:sensors_plus/sensors_plus.dart';
import 'dart:async';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: SensorBallScreen(),
    );
  }
}

class SensorBallScreen extends StatefulWidget {
  const SensorBallScreen({super.key});

  @override
  State<SensorBallScreen> createState() => _SensorBallScreenState();
}

class _SensorBallScreenState extends State<SensorBallScreen> {
  // Posición inicial
  double x = 150;
  double y = 300;

  // Velocidades
  double vx = 0;
  double vy = 0;

  final double ballSize = 30;
  StreamSubscription<AccelerometerEvent>? accelSub;

  @override
  void initState() {
    super.initState();

    // CAMBIO CLAVE: Se usa accelerometerEventStream() con paréntesis
    accelSub = accelerometerEventStream().listen((AccelerometerEvent event) {
      if (!mounted) return;

      setState(() {
        // Gravedad por inclinación
        // Invertimos X porque al inclinar a la derecha el sensor da negativo
        vx -= event.x * 0.35; 
        vy += event.y * 0.35;

        // Fricción (para que no se descontrole)
        vx *= 0.96;
        vy *= 0.96;

        x += vx;
        y += vy;

        // Obtener tamaño de pantalla para los límites
        final size = MediaQuery.of(context).size;
        final double maxWidth = size.width - ballSize;
        final double maxHeight = size.height - ballSize;

        // Rebotes y límites
        if (x < 0) {
          x = 0;
          vx *= -0.5; // Rebote con pérdida de energía
        } else if (x > maxWidth) {
          x = maxWidth;
          vx *= -0.5;
        }

        if (y < 0) {
          y = 0;
          vy *= -0.5;
        } else if (y > maxHeight) {
          y = maxHeight;
          vy *= -0.5;
        }
      });
    });
  }

  @override
  void dispose() {
    // Es vital cancelar la suscripción para no gastar batería
    accelSub?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF121212),
      body: Stack(
        children: [
          // Un pequeño texto decorativo
          const Center(
            child: Text(
              "Inclina tu teléfono",
              style: TextStyle(color: Colors.white24, fontSize: 20),
            ),
          ),
          // La bolita
          Positioned(
            left: x,
            top: y,
            child: Container(
              width: ballSize,
              height: ballSize,
              decoration: BoxDecoration(
                color: Colors.redAccent,
                shape: BoxShape.circle,
                boxShadow: [
                  BoxShadow(
                    color: Colors.redAccent.withOpacity(0.5),
                    blurRadius: 10,
                    spreadRadius: 2,
                  )
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}