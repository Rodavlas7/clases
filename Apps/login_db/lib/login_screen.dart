import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'register_screen.dart';
import 'success_screen.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final userController = TextEditingController();
  final passController = TextEditingController();
  String message = '';

  Future<void> login() async {
    var url = Uri.parse("http://TU_IP/login_flutter/login.php");

    var response = await http.post(url, body: {
      'username': userController.text,
      'password': passController.text,
    });

    if (response.body == "success") {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (_) => const SuccessScreen()),
      );
    } else {
      setState(() => message = "Usuario o contraseña incorrectos");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Login")),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(controller: userController, decoration: const InputDecoration(labelText: "Usuario")),
            const SizedBox(height: 16),
            TextField(controller: passController, obscureText: true, decoration: const InputDecoration(labelText: "Contraseña")),
            const SizedBox(height: 24),
            ElevatedButton(onPressed: login, child: const Text("Iniciar sesión")),
            TextButton(
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(builder: (_) => const RegisterScreen()));
              },
              child: const Text("No tengo cuenta"),
            ),
            Text(message),
          ],
        ),
      ),
    );
  }
}
