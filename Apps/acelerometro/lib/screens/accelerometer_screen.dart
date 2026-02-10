import 'dart:async';
import 'package:sensors_plus/sensors_plus.dart'; 
import 'package:flutter/material.dart';


void main() => runApp(const AccelerometerScreen());

class AccelerometerScreen extends StatefulWidget {
  const AccelerometerScreen({super.key});

  @override
  State<AccelerometerScreen> createState() => _AccelerometerScreenState();
}

class _AccelerometerScreenState extends State<AccelerometerScreen> {
  double x = 0.0, y = 0.0, z = 0.0;
  StreamSubscription<AccelerometerEvent>? AccelerometerListener;

  @override
  void initState() {
    super.initState();
    AccelerometerListener = accelerometerEventStream().listen((AccelerometerEvent event) {
      setState(() {
        x = event.x;
        y = event.y;
        z = event.z;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Accelerometer Example'),
        centerTitle: true,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Mueve tu dispositivo', style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold),),// en negritas
            const SizedBox(height: 10),
            Text('X: ${x.toStringAsFixed(2)}', style: const TextStyle(fontSize: 22),),
            const SizedBox(height: 10),
            Text('Y: ${y.toStringAsFixed(2)}', style: const TextStyle(fontSize: 22),),
            const SizedBox(height: 10),
            Text('Z: ${z.toStringAsFixed(2)}', style: const TextStyle(fontSize: 22),),

          ],
        ),
      ),
    );
  }
}