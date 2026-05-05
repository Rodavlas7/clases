import 'dart:math';

import 'package:flutter/material.dart';
import 'package:pedometer/pedometer.dart';
import 'dart:async';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        primarySwatch: Colors.blueGrey,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      debugShowCheckedModeBanner: false,
      title: 'Material App',
      home: HomePage(),
    );
  }
}

//pedometer

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  int _steps = 0;
  String _status = 'Waiting for...';

  @override
  void initState() {
    super.initState();
    _iniciarPedometer();
  }

  void _iniciarPedometer() {
    // 1. Escuchar el conteo de pasos
    Pedometer.stepCountStream.listen(
      (event) {
        setState(() {
          _steps = event.steps;
        });
        print('Pasos: ${event.steps}');
      },
      onError: (error) {
        setState(() => _status = 'Error en pasos: $error');
      },
    ); 

    // 2. Escuchar si el usuario se mueve o está quieto
    Pedometer.pedestrianStatusStream.listen(
      (event) {
        setState(() {
          _status = event.status == 'walking' ? 'Caminando' : 'Quieto';
        });
        print('Estado: ${event.status}');
      },
      onError: (error) {
        setState(() => _status = 'Error en estado: $error');
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Pedometer Example'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Steps taken: $_steps', style: TextStyle(fontSize: 24)),
            SizedBox(height: 20),
            Text('Status: $_status', style: TextStyle(fontSize: 16)),
          ],
        ),
      ),
    );
  }
}

