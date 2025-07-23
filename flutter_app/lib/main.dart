import 'package:flutter/material.dart';

void main() {
  runApp(const EBeerApp());
}

class EBeerApp extends StatelessWidget {
  const EBeerApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'eBeer Mobile',
      theme: ThemeData(
        primarySwatch: Colors.green,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('eBeer Shop')),
      body: const Center(
        child: Text('Welcome to the eBeer mobile app'),
      ),
    );
  }
}
