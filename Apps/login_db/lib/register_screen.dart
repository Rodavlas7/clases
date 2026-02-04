import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});

  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  final userController = TextEditingController();
  final passController = TextEditingController();

  Future<void> register() async {
    var url = Uri.parse("http://TU_IP/login_flutter/register.php");

    await http.post(url, body: {
      'username': userController.text,
      'password': passController.text,
    });

    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Registro")),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: userController,
              decoration: const InputDecoration(labelText: "Usuario"),
            ),
            const SizedBox(height: 16),
            TextField(
              controller: passController,
              obscureText: true,
              decoration: const InputDecoration(labelText: "Contraseña"),
            ),
            const SizedBox(height: 24),
            ElevatedButton(
              onPressed: register,
              child: const Text("Registrarse"),
            ),
          ],
        ),
      ),
    );
  }
}
