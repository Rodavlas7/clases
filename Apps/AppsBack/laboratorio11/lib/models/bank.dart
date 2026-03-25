// models/bank.dart
class Bank {
  final int? id;
  final String name;
  final bool status; // Changed from Bool to bool

  Bank({this.id, required this.name, required this.status});

  factory Bank.fromJson(Map<String, dynamic> json) {
    return Bank(
      id: json['id'],
      name: json['name'],
      status: json['status'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'status': status,
    };
  }
}