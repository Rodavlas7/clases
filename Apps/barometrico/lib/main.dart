import 'dart:async';
import 'package:flutter/material.dart';
import 'package:sensors_plus/sensors_plus.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Barómetro App',
      debugShowCheckedModeBanner: false,
      home: const BarometroHome(), 
    );
  }
}

class BarometroHome extends StatefulWidget {
  const BarometroHome({super.key});

  @override
  State<BarometroHome> createState() => _BarometroHomeState();
}

class _BarometroHomeState extends State<BarometroHome> {
  double _presion = 0.0;
  
  StreamSubscription<BarometerEvent>? _barometerSubscription;

  @override
  void initState() {
    super.initState();
    _barometerSubscription = barometerEventStream().listen(
      (BarometerEvent event) {
        setState(() {
          _presion = event.pressure; 
        });
      },
      onError: (error) {
        debugPrint("Error detectado: $error");
      },
    );
  }

  @override
  void dispose() {
    _barometerSubscription?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromARGB(255, 241, 198, 185),
      appBar: AppBar(
        title: const Text('Mi Barómetro'),
        backgroundColor: Colors.white70,
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(48),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Text(
                'Presión Atmosférica',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
              ),

              const SizedBox(height: 32),

              const Icon(
                Icons.compress,
                size: 100, 
                color: Color.fromARGB(255, 100, 80, 120),
              ),
              
              const SizedBox(height: 32),

              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(24),
                decoration: BoxDecoration(
                  color: const Color.fromARGB(255, 211, 179, 226),
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Colors.black26, width: 2),
                ),
                child: Column(
                  children: [
                    Text(
                      '${_presion.toStringAsFixed(2)}',
                      style: const TextStyle(
                        fontSize: 50, 
                        fontWeight: FontWeight.w900,
                        color: Colors.black87,
                      ),
                    ),
                    const Text(
                      'hPa (Hectopascales)',
                      style: TextStyle(fontSize: 16, fontWeight: FontWeight.w500),
                    ),
                  ],
                ),
              ),

              const SizedBox(height: 32),

              if (_presion == 0.0)
                const Card(
                  color: Colors.white54,
                  child: Padding(
                    padding: EdgeInsets.all(8.0),
                    child: Text(
                      'Intentando leer el sensor...\n(Asegúrate de usar un dispositivo físico)',
                      textAlign: TextAlign.center,
                      style: TextStyle(color: Colors.redAccent, fontSize: 12),
                    ),
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}