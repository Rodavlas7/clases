import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  
  String texto = '';
  final TextEditingController controlador = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Caja de texto')),
        body: Padding(
          padding: const EdgeInsets.all(32),
          child: Column(
            children: [
              TextField(
                controller: controlador,
                decoration: const InputDecoration(
                  labelText: 'Escribe algo',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 20),
              Text(texto),
            ],
          ),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () {
            setState(() {
              texto = controlador.text;
            });
          },
          child: const Icon(Icons.send),
        ),
      ),
    );
  }
}