import 'dart:async';
import 'package:flutter/material.dart';
import 'package:wakelock_plus/wakelock_plus.dart';
import 'package:audioplayers/audioplayers.dart';

enum TimerState { idle, running, finished }

class TimerPage extends StatefulWidget {
  const TimerPage({super.key});

  @override
  State<TimerPage> createState() => _TimerPageState();
}

class _TimerPageState extends State<TimerPage> {
  static const double startSeconds = 30.0;

  double secondsLeft = startSeconds;
  Timer? timer;

  TimerState state = TimerState.idle;

  final AudioPlayer player = AudioPlayer();

  void onTap() {
    switch (state) {
      case TimerState.idle:
      case TimerState.finished:
        // Primer toque: reset a 30, NO inicia
        resetTimer();
        break;

      case TimerState.running:
        // Si está corriendo y tocan → se reinicia y espera
        stopTimer();
        resetTimer();
        break;
    }
  }

  void startTimer() {
    WakelockPlus.enable();

    state = TimerState.running;

    timer = Timer.periodic(
      const Duration(milliseconds: 100),
      (t) {
        setState(() {
          secondsLeft -= 0.1;

          if (secondsLeft <= 0) {
            secondsLeft = 0;
            finishTimer();
          }
        });
      },
    );
  }

  void finishTimer() async {
    timer?.cancel();
    WakelockPlus.disable();

    state = TimerState.finished;

    await player.play(
      AssetSource('sounds/zelda_end.mp3'),
    );

    setState(() {});
  }

  void resetTimer() {
    timer?.cancel();
    WakelockPlus.disable();

    setState(() {
      secondsLeft = startSeconds;
      state = TimerState.idle;
    });
  }

  void stopTimer() {
    timer?.cancel();
    WakelockPlus.disable();
  }

  @override
  void dispose() {
    timer?.cancel();
    player.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        if (state == TimerState.idle) {
          // Segundo toque: inicia
          startTimer();
        } else {
          onTap();
        }
      },
      child: Scaffold(
        backgroundColor: Colors.black,
        body: Center(
          child: Text(
            secondsLeft.toStringAsFixed(1),
            style: const TextStyle(
              fontSize: 96,
              color: Colors.white,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
      ),
    );
  }
}
