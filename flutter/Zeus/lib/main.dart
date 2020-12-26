import 'package:Zeus/front.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Zeus',
      theme: ThemeData(scaffoldBackgroundColor: Colors.black),
      home: Front(),
    );
  }
}
