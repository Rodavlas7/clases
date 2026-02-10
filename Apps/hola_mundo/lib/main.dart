import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(title: 'Material App', home: LoginScreen());
  }
}

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController userController = TextEditingController();
  final TextEditingController passController = TextEditingController();

  String errorMessage = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Login Form FLutter App")),

      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              //Icon Form
              Image.asset('assets/images/choso.jpg', height: 120.0),
              const SizedBox(height: 24),

              //Title
              const Text(
                'Flutter form Login App',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 32),

              //Username Input
              TextField(
                controller: userController,
                decoration: InputDecoration(
                  labelText: "Username",
                  border: OutlineInputBorder(),
                  prefixIcon: Icon(Icons.person),
                ),
              ),
              const SizedBox(height: 24),

              //Password Input
              TextField(
                controller: passController,
                obscureText: true,
                decoration: InputDecoration(
                  labelText: "Password",
                  border: OutlineInputBorder(),
                  prefixIcon: Icon(Icons.lock),
                ),
              ),
              const SizedBox(height: 24),

              //Button Input
              ElevatedButton(
                onPressed: () {
                  if (userController.text.isEmpty ||
                      passController.text.isEmpty) {
                    setState(() {
                      errorMessage = 'User or password empty';
                    });
                  } else {
                    setState(() {
                      errorMessage = 'All data are correct filled';
                    });
                  }
                },
                style: ElevatedButton.styleFrom(
                  padding: const EdgeInsetsGeometry.symmetric(vertical: 16),
                ),
                child: const Text('Log in', style: TextStyle(fontSize: 16)),
              ),
              const SizedBox(height: 16),

              if (errorMessage.isNotEmpty)
                Text(
                  errorMessage,
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    color: Colors.black,
                    fontWeight: FontWeight.bold,
                  ),
                ),

              const SizedBox(height: 12),

              //Final Text
              const Text(
                'Did you forgot your password?',
                textAlign: TextAlign.center,
                style: TextStyle(color: Colors.blue),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
