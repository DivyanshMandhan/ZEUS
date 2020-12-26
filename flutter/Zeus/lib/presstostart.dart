import 'package:Zeus/entry.dart';
import 'package:flutter/material.dart';

/*class presstostart extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: GestureDetector(
          onTap: () =>
              Navigator.of(context).push(MaterialPageRoute(builder: (context) {
            return secondpage();
          })),
          child: Image(
            image: AssetImage('assets/zeus_start.png'),
          ),
        ),
      ),
    );
  }
}*/
class Presstostart extends StatefulWidget {
  @override
  _PresstostartState createState() => _PresstostartState();
}

class _PresstostartState extends State<Presstostart>
    with SingleTickerProviderStateMixin {
  AnimationController _controller;

  @override
  void initState() {
    _controller =
        AnimationController(vsync: this, duration: Duration(seconds: 1));
    _controller.repeat();
    super.initState();
  }

  @override
  void dispose() {
    super.dispose();
    _controller.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () => Future.value(false),
      child: Padding(
          padding: const EdgeInsets.only(top: 50.0),
          child: Column(children: <Widget>[
            Padding(
              padding: const EdgeInsets.only(top: 50.0),
              child: Align(
                heightFactor: 0.826,
                alignment: Alignment.topLeft,
                child: Image(
                  image: AssetImage('assets/zeus_start.png'),
                ),
              ),
            ),
            FadeTransition(
              opacity: _controller,
              child: MaterialButton(
                onPressed: () {
                  Navigator.push(context,
                      new MaterialPageRoute(builder: (context) => Entry()));
                },
                child: Align(
                  heightFactor: 3.5,
                  alignment: Alignment.bottomCenter,
                  child: Text(
                    "PRESS TO START",
                    style: TextStyle(
                        fontSize: 30,
                        color: Colors.white,
                        shadows: [
                          Shadow(
                              color: Colors.yellow[400],
                              offset: Offset(3, 1),
                              blurRadius: 2)
                        ]),
                  ),
                ),
              ),
            )
          ])),
    );
  }
}
