import 'package:flutter/material.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:intl/intl.dart';

void main() {
  runApp(AlarmClockApp());
}

class AlarmClockApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Alarm Clock',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  FlutterLocalNotificationsPlugin flutterLocalNotificationsPlugin =
      FlutterLocalNotificationsPlugin();

  List<Alarm> alarms = [];

  @override
  void initState() {
    super.initState();
    initializeNotifications();
  }

  void initializeNotifications() {
    final initializationSettingsAndroid =
        AndroidInitializationSettings('@mipmap/ic_launcher');
    final initializationSettings =
        InitializationSettings(android: initializationSettingsAndroid);
    flutterLocalNotificationsPlugin.initialize(initializationSettings);
  }

  void setAlarm(DateTime dateTime) {
    final androidPlatformChannelSpecifics = AndroidNotificationDetails(
        'alarm_notif', 'alarm_notif', 'Channel for Alarm notification',
        icon: '@mipmap/ic_launcher',
        sound: RawResourceAndroidNotificationSound('alarm_tone'),
        largeIcon: DrawableResourceAndroidBitmap('@mipmap/ic_launcher'));

    final platformChannelSpecifics =
        NotificationDetails(android: androidPlatformChannelSpecifics);

    flutterLocalNotificationsPlugin.schedule(
        0,
        'Alarm',
        'It\'s time!',
        dateTime,
        platformChannelSpecifics);

    setState(() {
      alarms.add(Alarm(time: dateTime, enabled: true));
    });
  }

  void showTimePicker() async {
    final TimeOfDay? pickedTime = await showTimePicker(
      context: context,
      initialTime: TimeOfDay.now(),
    );

    if (pickedTime != null) {
      final now = DateTime.now();
      final selectedTime = DateTime(now.year, now.month, now.day,
          pickedTime.hour, pickedTime.minute);

      setAlarm(selectedTime);
    }
  }

  String formatTime(DateTime dateTime) {
    final format = DateFormat.jm();
    return format.format(dateTime);
  }

  @override
  Widget build(BuildContext context) {
    final now = DateTime.now();
    final formattedTime = DateFormat('hh:mm:ss a').format(now);

    return Scaffold(
      appBar: AppBar(
        title: Text('Alarm Clock'),
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Text(
              'Current Time: $formattedTime',
              style: TextStyle(fontSize: 24),
            ),
          ),
          ElevatedButton(
            onPressed: showTimePicker,
            child: Text('Set Alarm'),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: alarms.length,
              itemBuilder: (context, index) {
                final alarm = alarms[index];
                return ListTile(
                  title: Text(formatTime(alarm.time)),
                  trailing: Switch(
                    value: alarm.enabled,
                    onChanged: (value) {
                      setState(() {
                        alarm.enabled = value;
                      });
                    },
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}

class Alarm {
  DateTime time;
  bool enabled;

  Alarm({required this.time, required this.enabled});
}

