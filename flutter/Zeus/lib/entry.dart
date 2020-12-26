import 'dart:async';

import 'package:Zeus/listening.dart';
import 'package:video_player/video_player.dart';
import 'package:flutter/material.dart';

class Entry extends StatefulWidget {
  @override
  _EntryState createState() => _EntryState();
}

class _EntryState extends State<Entry> {
  VideoPlayerController _controller;
  String screentext = "";
  String subtext = "";
  Timer timer;

  @override
  void initState() {
    super.initState();

    _controller = VideoPlayerController.network(
        'https://video5618.s3.us-east-2.amazonaws.com/zeus_entry_1.mp4')
      ..initialize().then((_) {
        // Ensure the first frame is shown after the video is initialized, even before the play button has been pressed.
        setState(() {});
      });
    _controller.play();
    _controller.setLooping(false);
    _controller.setVolume(1);
    Timer.periodic(Duration(seconds: 22), (Timer t) {
      setState(() {
        screentext = "ZEUS";
        subtext = "BOW BEFORE THE AlMIGHTY";
      });
    });
    startTime();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
          body: Stack(
        fit: StackFit.expand,
        children: <Widget>[
          Container(
            child: _controller.value.initialized
                ? AspectRatio(
                    aspectRatio: _controller.value.aspectRatio,
                    child: VideoPlayer(_controller),
                  )
                : Container(),
          ),
          Column(
            mainAxisAlignment: MainAxisAlignment.end,
            children: <Widget>[
              Padding(
                  padding: EdgeInsets.only(left: 16.0, right: 16.0),
                  child: Container(
                      child: Text(
                    screentext,
                    style: TextStyle(
                        color: Colors.white,
                        fontSize: 60.0,
                        shadows: [
                          Shadow(
                              color: Colors.black,
                              offset: Offset(4, 2),
                              blurRadius: 2)
                        ]),
                  ))),
              Padding(
                  padding: EdgeInsets.only(left: 16.0, right: 30.0),
                  child: Container(
                      child: Text(
                    subtext,
                    style: TextStyle(color: Colors.white70, fontSize: 20.0),
                  ))),
              SizedBox(height: 20.0),
              Padding(
                padding: EdgeInsets.only(left: 16.0, right: 16.0),
                child: Container(
                  width: MediaQuery.of(context).size.width,
                  child: RaisedButton(
                    onPressed: () {
                      Navigator.push(
                          context,
                          new MaterialPageRoute(
                              builder: (context) => Listening()));
                      _controller.pause();
                    },
                    shape: RoundedRectangleBorder(
                        borderRadius: new BorderRadius.circular(30.0)),
                    child: Text("SKIP"),
                    color: Colors.yellow,
                    textColor: Colors.black,
                    padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                    splashColor: Colors.grey,
                  ),
                ),
              ),
            ],
          )
        ],
      )),
    );
  }

  startTime() async {
    var duration = new Duration(seconds: 38);
    return new Timer(duration, route);
  }

  route() {
    Navigator.pushReplacement(
        context, MaterialPageRoute(builder: (context) => Listening()));
  }

  @override
  void dispose() {
    super.dispose();
    _controller.dispose();
  }
}
