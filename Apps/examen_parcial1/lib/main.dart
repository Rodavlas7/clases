import 'package:flutter/material.dart';
import 'Pantalla2.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Material App',
      home: const LoginScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController usuario = TextEditingController(); //controlador de usuario

  String mensaje = '';
  

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromARGB(255, 241, 198, 185), //cambio el color del widjet scaffold
      appBar: AppBar(
        title: const Text('Inicio de Sesion'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(48),
        child: Center(
          child: Column(
            children: [

              const Text(
                'Inicio de Sesion',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
              ),

              const SizedBox(height: 32),

              Image.asset('assets/images/choso.jpg', height: 120),
              const SizedBox(height: 24),

              TextField( //campo de texto usuario
                controller: usuario,
                decoration: const InputDecoration(
                  labelText: 'Usuario',
                  border: OutlineInputBorder(),
                  prefixIcon: Icon(Icons.person_4),//icono repesentativo del usuario
                  fillColor: Color.fromARGB(255, 211, 179, 226), //color del campo
                  filled: true, //habilita el color del campo
                  hintText: 'Escriba su usuario', //texto de ayuda
                ),
              ),

              const SizedBox(height: 24), // espaciado entre campos

              ElevatedButton( //boton ingresar
                onPressed: () {
                  if (usuario.text.isEmpty) { //detecta si los campos estan vacios
                    setState(() {
                      mensaje = 'Campo usuario vacio';
                    });
                  } else { // si los campos estan llenos
                    setState(() { //actualiza el estado del widget
                      mensaje = 'Datos correctos';
                      usuario.clear(); //limpia los campos de texto
                    });
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => const Pantalla2(),//navega a la pantalla 2
                      ),
                    );
                  }
                },
                child: const Text('Ingresar', style: TextStyle(fontSize: 16)),
              ),

              const SizedBox(height: 24), //espaciado antes del mensaje

              if (mensaje.isNotEmpty)
                Text(
                  mensaje,
                  textAlign: TextAlign.center,
                  style: const TextStyle(fontWeight: FontWeight.bold),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

