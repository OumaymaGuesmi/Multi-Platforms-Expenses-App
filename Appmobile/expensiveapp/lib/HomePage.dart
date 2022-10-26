import 'package:flutter/material.dart';
import 'categories.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  int _selectedIndex = 0;
  List<Category> _categories = [
    Category('Health', Icons.health_and_safety, -1200),
    Category('Food', Icons.food_bank, -1300),
    Category('Gifts', Icons.card_giftcard, -1400),
  ];
  static const TextStyle optionStyle =
      TextStyle(fontSize: 30, fontWeight: FontWeight.bold);
  static const List<Widget> _widgetOptions = <Widget>[
    Text('hello'),
    Text('yoo'),
    Text('fdf')
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  void handleClick(String value) {
    switch (value) {
      case 'Logout':
        break;
      case 'Settings':
        break;
    }
  }

  Widget _buildCategoryCards(BuildContext context, int index) {
    return Container(
      padding: EdgeInsets.all(15.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            children: <Widget>[
              Icon(_categories[index].icon),
              Text(_categories[index].name),
            ],
          ),
          Text(
            _categories[index].value.toString(),
            style: TextStyle(color: Colors.red),
          ),
        ],
      ),
    );
  }

  Widget _buildCategoryCardsTodays(BuildContext context, int index) {
    return Container(
      padding: EdgeInsets.all(15.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            children: <Widget>[
              Icon(_categories[index].icon),
              Text(_categories[index].name),
            ],
          ),
          Text(
            _categories[index].value.toString(),
            style: TextStyle(color: Colors.red),
          ),
        ],
      ),
    );
  }

  @override
  Widget buildthreemain() {
    return Container(
      child: Column(children: [
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 20),
          child: Container(
            decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(8),
                color: Colors.white,
                border: Border.all(color: Color.fromARGB(255, 94, 95, 97))),
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 10),
              child: Row(
                children: [
                  Row(
                    children: [
                      Image.asset(
                        "assets/images/all1.png",
                        height: 100,
                        width: 100,
                      ),
                      Image.asset(
                        "assets/images/income.png",
                        height: 100,
                        width: 100,
                        fit: BoxFit.fitHeight,
                      ),
                      Image.asset(
                        "assets/images/outcome.png",
                        height: 100,
                        width: 100,
                      )
                    ],
                  ),
                ],
              ),
            ),
          ),
        ),
      ]),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: Container(
          padding: EdgeInsets.all(5),
          width: 40,
          child: Icon(
            Icons.monetization_on_rounded,
            color: Colors.blue,
          ),
        ),
        title: Padding(
          padding: const EdgeInsets.only(left: 30),
          child: Text("Expensive APP",
              style:
                  TextStyle(fontWeight: FontWeight.bold, color: Colors.black)),
        ),
        backgroundColor: Color.fromARGB(255, 35, 45, 233),
        actions: <Widget>[
          PopupMenuButton<String>(
            onSelected: handleClick,
            itemBuilder: (BuildContext context) {
              return {'Logout', 'Settings'}.map((String choice) {
                return PopupMenuItem<String>(
                  value: choice,
                  child: Text(choice),
                );
              }).toList();
            },
          ),
        ],
      ),
      body: Column(
        children: [
          buildthreemain(),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 20),
            child: Container(
              decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(8),
                  color: Colors.white,
                  border: Border.all(color: Color.fromARGB(255, 94, 95, 97))),
              child: Column(
                children: [
                  Text('CATEGORIES'),
                  _buildCategoryCards(context, 0),
                  _buildCategoryCards(context, 1),
                  _buildCategoryCards(context, 2),
                ],
              ),
            ),
          ),
          Column(
            children: [
              Padding(
                  padding:
                      const EdgeInsets.symmetric(horizontal: 10, vertical: 20),
                  child: Container(
                    decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(8),
                        color: Colors.white,
                        border:
                            Border.all(color: Color.fromARGB(255, 94, 95, 97))),
                    child: Column(
                      children: [
                        Text('TODAYS LOG'),
                        _buildCategoryCardsTodays(context, 0),
                        _buildCategoryCardsTodays(context, 1),
                        _buildCategoryCardsTodays(context, 2),
                      ],
                    ),
                  )),
              Center(
                child: _widgetOptions.elementAt(_selectedIndex),
              ),
            ],
          ),
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.dashboard_outlined),
            label: 'Features',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.settings),
            label: 'Settings',
          ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Color.fromARGB(255, 62, 62, 254),
        onTap: _onItemTapped,
      ),
    );
  }
}
