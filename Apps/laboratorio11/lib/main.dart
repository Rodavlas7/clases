import 'package:flutter/material.dart';
import 'models/bank.dart';
import 'services/api_service.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Material App',
      home: BankScreen(),
    );
  }
}

class BankScreen extends StatefulWidget {
  const BankScreen({super.key});

  @override
  State<BankScreen> createState() => _BankScreenState();
}

class _BankScreenState extends State<BankScreen> {

  late Future<List<Bank>> banks;

  @override
  void initState() {
    super.initState();
    banks = ApiService.obtenerBanks();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Bank Screen'),
      ),
      body: FutureBuilder<List<Bank>>(
        future: banks,
        builder: (context, snapshot){
          if (snapshot.hasData) {
            return ListView.builder(
              children: snapshot.data!.map(
                (p) => ListTile(
                  title: Text(p.name),
                  subtitle: Text(p.status),
                ).toList(),
              ),
            );

          } else if (snapshot.hasError){
            return Center(
              child: Text('Error: ${snapshot.error}'),
            );
          }
          return const Center(
            child: CircularProgressIndicator(),
          );
        }
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: {} async {
          await Apiservice.crearBank(
            Bank(name: "New Bank" , status: true)
          );
          setState(() {
            banks = ApiService.obtenerBanks();
          });
        },
      ),
    );
  }
}