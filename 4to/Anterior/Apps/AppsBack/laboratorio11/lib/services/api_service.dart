// services/api_service.dart
import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/bank.dart';

class ApiService {
  static const String baseUrl = "http://10.0.2.2:8000/api/banks/";

  // GET
  static Future<List<Bank>> obtenerBancos() async {
    final response = await http.get(Uri.parse(baseUrl));

    if (response.statusCode == 200) {
      List data = json.decode(response.body);
      return data.map((e) => Bank.fromJson(e)).toList();
    } else {
      throw Exception("Error al cargar bancos");
    }
  }

  // POST
  static Future<void> crearBanco(Bank bank) async { // Renamed to crearBanco
    final response = await http.post(
      Uri.parse(baseUrl),
      headers: {"Content-Type": "application/json"},
      body: json.encode(bank.toJson()),
    );

    if (response.statusCode != 201) {
      throw Exception("Error al crear banco");
    }
  }
}