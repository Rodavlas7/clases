import 'package:flutter/material.dart';
import 'dart:io';
import 'package:image_picker/image_picker.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart' as p;
import 'package:shared_preferences/shared_preferences.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Material App',
      debugShowCheckedModeBanner: false,
      home: PhotoTaker(),
    );
  }
}

class PhotoTaker extends StatefulWidget {
  const PhotoTaker({super.key});

  @override
  State<PhotoTaker> createState() => _PhotoTakerState();
}

class _PhotoTakerState extends State<PhotoTaker> {
  File? _archivoImagen;
  final ImagePicker _selectorImagen = ImagePicker();

  @override
  void initState() {
    super.initState();
    cargarImagen();
  }

  Future<void> capturarImagen() async {
    final XFile? imagenTemporal = await _selectorImagen.pickImage(
      source: ImageSource.camera,
    );

    if (imagenTemporal != null) {
      final directorio = await getApplicationDocumentsDirectory();
      final String nombreArchivo = p.basename(imagenTemporal.path);
      final String rutaFinal = '${directorio.path}/$nombreArchivo';

      final File imagenGuardada =
          await File(imagenTemporal.path).copy(rutaFinal);

      final prefs = await SharedPreferences.getInstance();
      await prefs.setString('ruta_imagen', imagenGuardada.path);

      setState(() {
        _archivoImagen = imagenGuardada;
      });

      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Foto Guardada!')),
      );
    }
  }

  Future<void> cargarImagen() async {
    final prefs = await SharedPreferences.getInstance();
    final String? ruta = prefs.getString('ruta_imagen');

    if (ruta != null && File(ruta).existsSync()) {
      setState(() {
        _archivoImagen = File(ruta);
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Camera App'),
        centerTitle: true,
      ),
      body: Center(
        child: _archivoImagen == null
            ? const Text('No image selected.')
            : Image.file(_archivoImagen!),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: capturarImagen,
        child: const Icon(Icons.camera_alt),
      ),
    );
  }
}