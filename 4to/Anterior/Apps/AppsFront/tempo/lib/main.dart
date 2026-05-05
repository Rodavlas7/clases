import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:wakelock_plus/wakelock_plus.dart';
import 'package:audioplayers/audioplayers.dart';

void main() {
  runApp(const TimerApp());
}

class TimerApp extends StatelessWidget {
  const TimerApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: CountdownScreen(),
    );
  }
}

class CountdownScreen extends StatefulWidget {
  const CountdownScreen({super.key});

  @override
  State<CountdownScreen> createState() => _CountdownScreenState();
}

class _CountdownScreenState extends State<CountdownScreen> {
  static const double startSeconds = 30.0;

  double secondsLeft = startSeconds;
  Timer? timer;

  bool isRunning = false;
  bool isTimeUp = false;

  final AudioPlayer _audioPlayer = AudioPlayer();

  final List<String> naviSounds = [
    'sounds/OOT_Navi_Listen1.wav',
    'sounds/OOT_Navi_Listen2.wav',
    'sounds/OOT_Navi_Listen3.wav',
    'sounds/OOT_Navi_Listen4.wav',
    'sounds/OOT_Navi_Listen5.wav',
    'sounds/OOT_Navi_Hey1.wav',
    'sounds/OOT_Navi_Hey2.wav',
    'sounds/OOT_Navi_Hey3.wav',
    'sounds/OOT_Navi_Hey4.wav',
    'sounds/OOT_Navi_Hey5.wav',
  ];

  @override
  void initState() {
    super.initState();

    // Pantalla completa real
    SystemChrome.setEnabledSystemUIMode(SystemUiMode.immersiveSticky);
  }

  void onScreenTap() {
    // Si terminó el tiempo va a resetear a 30 y esperar
    if (isTimeUp) {
      resetTimer();
      return;
    }

    // Si NO está corriendo va a iniciar
    if (!isRunning) {
      startTimer();
    } else {
      // Si está corriendo va a resetear a 30 y detener
      resetTimer();
    }
  }

  void startTimer() {
    WakelockPlus.enable();

    timer?.cancel();
    isRunning = true;

    timer = Timer.periodic(const Duration(milliseconds: 100), (t) {
      setState(() {
        secondsLeft -= 0.1;

        if (secondsLeft <= 0) {
          secondsLeft = 0;
          t.cancel();
          isRunning = false;
          isTimeUp = true;

          WakelockPlus.disable();
          playRandomNaviSound();
        }
      });
    });
  }

  void resetTimer() {
    timer?.cancel();
    WakelockPlus.disable();

    setState(() {
      secondsLeft = startSeconds;
      isRunning = false;
      isTimeUp = false;
    });
  }

  void playRandomNaviSound() {
    final random = Random();
    final sound = naviSounds[random.nextInt(naviSounds.length)];
    _audioPlayer.play(AssetSource(sound));
  }

  @override
  void dispose() {
    timer?.cancel();
    _audioPlayer.dispose();
    WakelockPlus.disable();

    // Restaurar UI del sistema
    SystemChrome.setEnabledSystemUIMode(SystemUiMode.edgeToEdge);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      behavior: HitTestBehavior.opaque,
      onTap: onScreenTap,
      child: Scaffold(
        backgroundColor: isTimeUp ? Colors.red : Colors.black,
        body: Center(
          child: Text(
            secondsLeft.toStringAsFixed(1),
            style: const TextStyle(
              fontSize: 120,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
        ),
      ),
    );
  }
}
