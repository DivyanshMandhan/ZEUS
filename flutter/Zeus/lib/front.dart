import 'dart:async';
import 'package:Zeus/presstostart.dart';
import 'package:flutter/material.dart';

/*class front extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () => Future.value(false),
      child: Scaffold(
        body: Center(
          child: GestureDetector(
            onTap: () => Navigator.of(context)
                .push(new MaterialPageRoute(builder: (context) {
              return secondpage();
            })),
            child: Image(
              image: AssetImage('assets/zeus_front.png'),
            ),
          ),
        ),
      ),
    );
  }
}*/
class Front extends StatefulWidget {
  @override
  _FrontState createState() => _FrontState();
}

class _FrontState extends State<Front> with SingleTickerProviderStateMixin {
  AnimationController _controller;
  Animation<double> animation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: Duration(milliseconds: 4000),
    );
    animation = CurvedAnimation(parent: _controller, curve: Curves.easeIn);
    _controller.repeat();

    startTime();
  }

  @override
  void dispose() {
    super.dispose();
    _controller.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: initScreen(context),
    );
  }

  startTime() async {
    var duration = new Duration(seconds: 5);
    return new Timer(duration, route);
  }

  route() {
    Navigator.pushReplacement(
        context, MaterialPageRoute(builder: (context) => Presstostart()));
  }

  initScreen(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            FadeTransition(
                opacity: animation,
                child: Image(
                  image: AssetImage('assets/zeus_front.png'),
                )),
          ],
        ),
      ),
    );
  }
}
