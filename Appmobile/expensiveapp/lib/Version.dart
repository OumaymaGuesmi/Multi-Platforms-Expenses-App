import 'SignupScreen.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'SignUpScreenOffline.dart';

class Version extends StatefulWidget {
  const Version({super.key});

  @override
  State<Version> createState() => _VersionState();
}

class _VersionState extends State<Version> {
  @override
  Widget buildOfflineBtn() {
    return Container(
        padding: EdgeInsets.symmetric(vertical: 25),
        width: double.infinity,
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(
              primary: Colors.white, // background
              onPrimary: Colors.white, // foreground
              padding: EdgeInsets.all(15),
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15))),
          onPressed: ()=> {
              Navigator.push(
                  context,MaterialPageRoute(builder: (context) => const SignUpScreenOffline())),
          },
          child: Text(
            'Offline',
            style: TextStyle(
                color: Color.fromARGB(255, 54, 6, 226),
                fontSize: 18,
                fontWeight: FontWeight.bold),
          ),
        ));
  }

  Widget buildOnlineBtn() {
    return Container(
        padding: EdgeInsets.symmetric(vertical: 25),
        width: double.infinity,
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(
              primary: Colors.white, // background
              onPrimary: Colors.white, // foreground
              padding: EdgeInsets.all(15),
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15))),
          onPressed: () => Navigator.push(
              context, MaterialPageRoute(builder: (_) => const SignupScreen())),
          child: Text(
            'Online',
            style: TextStyle(
                color: Color.fromARGB(255, 54, 6, 226),
                fontSize: 18,
                fontWeight: FontWeight.bold),
          ),
        ));
  }

  Widget build(BuildContext context) {
    return Scaffold(
      body: AnnotatedRegion<SystemUiOverlayStyle>(
        value: SystemUiOverlayStyle.light,
        child: GestureDetector(
          child: Stack(
            children: <Widget>[
              SizedBox(
                height: 20,
              ),
              Container(
                  height: double.infinity,
                  width: double.infinity,
                  decoration: BoxDecoration(
                    color: Color.fromARGB(255, 65, 105, 225),
                    image: DecorationImage(
                        image: new AssetImage("assets/images/logo.png"),
                        alignment: Alignment.topCenter,
                        scale: 1.8),
                  ),
                  child: SingleChildScrollView(
                    physics: AlwaysScrollableScrollPhysics(),
                    padding:
                        EdgeInsets.symmetric(horizontal: 25, vertical: 230),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        Text(
                          'What version do you want to use ?',
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 40,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        SizedBox(height: 10),
                        buildOfflineBtn(),
                        SizedBox(height: 10),
                        buildOnlineBtn()
                      ],
                    ),
                  ))
            ],
          ),
        ),
      ),
    );
  }
}
