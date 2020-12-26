import 'dart:async';

import 'package:avatar_glow/avatar_glow.dart';
import 'package:flutter/material.dart';

import 'package:highlight_text/highlight_text.dart';
import 'package:speech_to_text/speech_to_text.dart' as stt;
import 'package:url_launcher/url_launcher.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:http/http.dart' as http;

final FlutterTts flutterTts = FlutterTts();

class Listening extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () => Future.value(false),
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
            primarySwatch: Colors.grey, scaffoldBackgroundColor: Colors.black),
        home: Listen(),
      ),
    );
  }
}

class Listen extends StatefulWidget {
  @override
  _ListenState createState() => _ListenState();
}

class _ListenState extends State<Listen> {
  String url;
  var data;
  String QueryText = 'Query';
  final Map<String, HighlightedWord> _highlights = {
    'Zeus': HighlightedWord(
      onTap: () => print('Zeus'),
      textStyle: const TextStyle(
        fontSize: 40.0,
        color: Colors.red,
        fontWeight: FontWeight.bold,
      ),
    ),
    'God': HighlightedWord(
      onTap: () => print('God'),
      textStyle: const TextStyle(
        fontSize: 40.0,
        color: Colors.yellow,
        fontWeight: FontWeight.bold,
      ),
    ),
    'thunder': HighlightedWord(
      onTap: () => print('thunder'),
      textStyle: const TextStyle(
        fontSize: 40.0,
        color: Colors.yellow,
        fontWeight: FontWeight.bold,
      ),
    ),
    'hello': HighlightedWord(
      onTap: () => print('hello'),
      textStyle: const TextStyle(
        fontSize: 40.0,
        color: Colors.lightGreen,
        fontWeight: FontWeight.bold,
      ),
    ),
    'game': HighlightedWord(
      onTap: () => print('game'),
      textStyle: const TextStyle(
        fontSize: 40.0,
        color: Colors.blueAccent,
        fontWeight: FontWeight.bold,
      ),
    ),
    'Google': HighlightedWord(
      onTap: () => print('Google'),
      textStyle: const TextStyle(
        fontSize: 40.0,
        color: Colors.pink,
        fontWeight: FontWeight.bold,
      ),
    ),
    'YouTube': HighlightedWord(
      onTap: () => print('YouTube'),
      textStyle: const TextStyle(
        fontSize: 40.0,
        color: Colors.red,
        fontWeight: FontWeight.bold,
      ),
    ),
    'WhatsApp': HighlightedWord(
      onTap: () => print('WhatsApp'),
      textStyle: const TextStyle(
        fontSize: 40.0,
        color: Colors.green,
        fontWeight: FontWeight.bold,
      ),
    ),
  };

  stt.SpeechToText _speech;
  bool _isListening = false;
  String _text = 'Press to Call Zeus';
  double _confidence = 1.0;

  @override
  void initState() {
    super.initState();
    _speech = stt.SpeechToText();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('I am sure: ${(_confidence * 100.0).toStringAsFixed(1)}%'),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      floatingActionButton: AvatarGlow(
        animate: _isListening,
        glowColor: Theme.of(context).primaryColor,
        endRadius: 75.0,
        duration: const Duration(milliseconds: 2000),
        repeatPauseDuration: const Duration(milliseconds: 100),
        repeat: true,
        child: FloatingActionButton(
          onPressed: _listen,
          child: Icon(_isListening ? Icons.mic : Icons.mic_none),
        ),
      ),
      body: SingleChildScrollView(
          reverse: true,
          child: Column(
            children: [
              Padding(
                padding: const EdgeInsets.only(top: 50.0),
                child: Align(
                  heightFactor: 1.5,
                  alignment: Alignment.center,
                  child: Image(
                    image: AssetImage('assets/launch.png'),
                  ),
                ),
              ),
              Container(
                padding: const EdgeInsets.fromLTRB(30.0, 30.0, 30.0, 150.0),
                child: TextHighlight(
                  text: _text,
                  words: _highlights,
                  textStyle: const TextStyle(
                    fontSize: 40.0,
                    color: Colors.white,
                    fontWeight: FontWeight.w400,
                  ),
                ),
              ),
            ],
          )),
    );
  }

  void _listen() async {
    if (!_isListening) {
      bool available = await _speech.initialize(
        onStatus: (val) => print('onStatus: $val'),
        onError: (val) => print('onError: $val'),
      );
      if (available) {
        setState(() => _isListening = true);
        _speech.listen(
          onResult: (val) => setState(() {
            _text = val.recognizedWords;
            if (val.hasConfidenceRating && val.confidence > 0) {
              _confidence = val.confidence;
            } else if (_speech.lastRecognizedWords == 'open YouTube') {
              flutterTts.speak("Opening Youtube");
              launch("https://www.youtube.com");
              //opening in browser
              url = "http://192.168.29.194:5000/api?Query=open%20youtube";
              Getdata(url);
            } else if (_speech.lastRecognizedWords == 'open Google') {
              flutterTts.speak("Opening Google");
              launch("https://google.com");
              //opening in browser
              url = "http://192.168.29.194:5000/api?Query=open%20google";
              Getdata(url);
            } else if (_speech.lastRecognizedWords == 'WhatsApp me') {
              final String phone = "917060164066";
              launch("whatsapp://send?phone=$phone");
              flutterTts.speak("sending message to you");
            }
          }),
        );
      }
    } else {
      setState(() => _isListening = false);
      _speech.stop();
    }
  }
}

Future Getdata(url) async {
  http.Response Response = await http.get(url);
  return Response.body;
}
