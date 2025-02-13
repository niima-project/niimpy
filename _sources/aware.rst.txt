Aware
=====

You can read upstream information about Aware sensors from
http://www.awareframework.com/sensors/ .  This page elaborates the
material found there, in particular how the `koota-server
<https://github.com/digitraceslab/koota-server/>`__ project processes
the data.  Still, most of this information could be a useful hints to
others using the Aware data.

You can find our previous information `on the koota-server wiki
<https://github.com/digitraceslab/koota-server/wiki/Aware#data-notes>`__,
but this information is now being moved here.

Section names in general correspond to the koota-server converter
name.


Standard columns
----------------

Some columns that are stored in all the tables.

* ``time``: unixtime, time of observation.
* ``datetime``: time when the data instance was collected.
* ``user``: a unique key to identify a user.
* ``device``: a unique key to identify a mobile device.


AwareAccelerometer
------------------

Accelerometer data is collected using the
phones’ accelerometer sensors. The data is used to measure the acceleration 
of the the phone in any direction of the 3D environment. The
coordinate-system is defined relative to the screen of the phone in its default 
orientation (facing the user). The axis are not swapped when the
device’s screen orientation changes. The X axis is horizontal and points
to the right, the Y axis is vertical and points up and the Z axis points
towards the outside of the front face of the screen. In this system, coordinates 
behind the screen have negative Z axis. The accelerometer sensor
measures acceleration and inclues the acceleration due to the force of gravity 
into consideration. So, if the phone is idle, the accelerometer reads the
acceleration of gravity 9.81m/s and if the phone is in free-fall towards the
ground, the accelerometer reads 0m/s. The frequency of the data collected can 
vary largely. It can be in the range of 0 to hundreds of data instances per hour.

* ``double_values_0``: acceleration values of X axis.
* ``double_values_1``: acceleration values of Y axis.
* ``double_values_2``: acceleration values of Z axis.

AwareApplicationCrashes
-----------------------

Contains information about crashed applications. This data is logged whenever any
application crashes, which can occur from zero to several times per hour.

* ``application_name``: application’s localized name.
* ``package_name``: application’s package name.
* ``error_short``: short description of the error.
* ``error_long``: more verbose version of the error description.
* ``application_version``: version code of the crashed application.
* ``error_condition``: type of error has occurred to the application. 1=code error, 2=Application Not Responding (ANR) error

AwareApplicationNotifications
-----------------------------

Contains the log of notifications the device has received. This data is logged whenever the phone receives a
notification so the frequency of this data can range from zero to hundreds of times per hour. 

* ``application_name``: application’s localized name.
* ``package_name``: application’s package name.
* ``sound``: notification’s sound source.
* ``vibrate``: notification’s vibration patterns.
* ``defaults``: 0=default color, -1=default all, 1=default sound, 2=default vibrate, 3=?, 4=default lights, 6=?, 7=?

AwareBattery
------------

Provides information about the battery and monitors power related events such as phone 
shutting down or rebooting or charging. The frequency of data sent by battery sensor can be from 0 to tens of times per hour.

* ``battery_level``: marks the current percentage of battery charge remaining.
* ``battery_status``: 1=unknown, 2=charging, 3=discharging, 4=not charging, 5=full, -1=shut down, -3=reboot.
* ``battery_health``: 1=unknown, 2=good, 3=overheat, 4=dead, 5=over voltage, 6=unspecified failure, 7=unknown, 9=?.
* ``batery_adaptor``: 0=?, 1=AC, 2=USB, 4=wireless adaptor.

AwareCalls
------------

Logs incoming and outgoing call details. The frequency of AwareMessages data depends upon number of calls
the users get so it can be from 0 to tens of times per hour.

* ``call_type``: 'incoming', 'outgoing', 'missed'.
* ``call_duration``: call duration in seconds.
* ``trace``: SHA-1 one-way source/target of the call.


AwareESM
--------

This table provides information about the ESM sensor which
adds support for user-provided context by leveraging mobile Experience
Sampling Method (ESM). The ESM questionnaires can be triggered by
context, time or on-demand, locally or remotely (within your study on
AWARE’s dashboard). Although user-subjective, this sensor allows crowd
sourcing information that is challenging to instrument with sensors. Depending upon the
number of time the users attempt to answer the questions, the frequency
can vary from 0 to tens of times per hour.

* ``time_asked``: unixtime of the moment the question was asked.
* ``id``: the id of the question asked.
* ``answer``: the answer to the question asked.
* ``type``: 1=text, 2=radio buttons, 3=checkbox, 4=likert scale, 5=quich answer, 6=scale, 9=numeric, 10=web.
* ``title``: title of the ESM.
* ``instructions``: instructions to answer the ESM.
* ``submit``: status of the submission.
* ``notification_timeout``: time after which the ESM notification is dismissed and the whole ESM queue
expires (in case expiration threshold is set to 0).

AwareLocationDayOld
-------------------

This table takes one-day chunks of data and does some processing, for cases where we can't give raw location data. A day goes from 04:00 one day to 04:00 the next day. Since the information is reliant upon location services being enabled, the frequency can range from zero to several thousands per hour.
* ``day``: day which is being analyzed, format YYYY-MM-DD.
* ``totdist``: total distance traveled during the day, meters.
* ``locstd``: radius of gyration (standard deviation of location throughout the day), meters.
* ``n_bins``: number of 10-minute intervals with data, including things.
* ``n_bins_nonnan``: number of these 10-minute intervals with data.
* ``transtime``: does not work (was supposed to be amount of time you are moving between clusters).
* ``numclust``: does not work (number of clusters determined with a k-means algorithm, in other words the number of locations they visited. Number of clusters increased until maximum radius is 500m. But maximum number of clusters is 20. This measure may not be accurate).
* ``entropy``: does not work (was supposed to be p*log(p) of all the cluster memberships.
* ``normentropy``: does not work.


AwareLocationDay
----------------

This table takes one-day chunks of data and does some processing, for cases where we can't give raw location data. A day goes from 04:00 one day to 04:00 the next day. Since the information is reliant upon location services being enabled, the frequency can range from zero to several thousands per hour.
* ``day``: day which is being analyzed, format YYYY-MM-DD.
* ``n_points``: the number of raw datapoints.
* ``n_bins_nonnan``: number of these 10-minute intervals with data.
* ``n_bins_paired``: the number of bins that also have data right after them.
* ``ts_min``: first timestamp of any data point of the day (unixtime seconds)
* ``ts_max``: last timestamp of any data point of the day (unixtime seconds)" (subtracting these two gives the range of data covered which can be contrasted with the next item)
* ``ts_std``: standard deviation of all timestamps (seconds)". Note that standard deviations of timestamps doesn't actually make that much sense, but combined with the range of timestamps can give you an idea of how spread out through the day the data points are.
* ``totdist``: total distance covered throughout the day, looking at only the binned averages. If there are large gaps in data, pretend those gaps don't exist and find the distances anyway (meters).
* ``totdist_raw``: total distance considering every data point (not binned). Probably larger than totdist, more affected by random fluctuations (meters).
* ``locstd``: Radius of gyration of locations, after the binning (meters).
* ``radius_mean``: this isn't exactly a radius, but the longest distance between any point and the mean location (both mean location and other points after binning). This measure may not make the most sense, but can be compared to locstd.
* ``diameter``: Not implemented, always nan.
* ``n_bins_moving``: number of bins which are considered to be moving. Each bin is compared to the one after to determine an average speed, and n_bins_moving is the number of bins above some threshold.
* ``n_bins_moving_speed``: number of bins which are moving, using the self-reported speed from Aware. Probably more accurate than the previous.
* ``n_points_moving_speed``: number of data points (non-binned) which are have a speed above the speed threshold.


AwareLocationSafe
-----------------

This table provides information about the users’ current location. Since the information is reliant upon location services being enabled, the frequency can range from zero to several thousands per hour.

* ``accuracy``: approximate accuracy of the location in meters.
* ``double_speed``: users’ speed in meters/second over the ground.
* ``double_bearing``: location’s bearing, in degrees.
* ``provider``: describes whether the location information was provided by network or GPS.
* ``label``: provides information whether location services was enabled or disabled.


AwareMessagess
--------------

Logs incoming and outgoing message details. The frequency of AwareMessages data depends upon number of messages the users get so it can be from 0 to tens of times per hour.

* ``message_type``: 'incoming', 'outgoing'.
* ``trace``: SHA-1 one-way source/target of the call.


AwareScreen
-----------

This table provides information about the screen status. The number of times this data is collected can range from zero to several hundreds per hour.

* ``screen_status``: 0=off, 1=on, 2=locked, 3=unlocked.


AwareTimestamps
---------------

This table lists all the timestamps collected from every data packet that was sent. The frequency of data, since logged for every data packet sent, can range from 0 to tens of thousands per hour.

* ``packet_time``: the unixtime of the moment each packet was sent.
* ``table``: provides information about which table did the data packet belong to. In other words it describes the kind of data that was being transferred in the packet.




Survey
------

Provides details about the active data collected from the participants in the form of questionnaires. The survey tables are given below.


MMMBackgroundAnswers, MMMBaselineAnswers, MMMDiagnosticPatientAnswers, MMMFeedbackPostActiveAnswers, MMMPostActiveAnswers, MMMSurveyAllAnswers
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

These 6 tables provide details about questions and answers that were asked to the participants of this study. The answers in each of these 6 tables were collected only once per user.

* ``id``: uniquely identifies which question was asked to the participant.
* ``access_time``: unixtime of the moment when the participant started answering the questions.
* ``question``: describes the question that was asked.
* ``answer``: provides the participants’ answer to the questions. The answers can be of several types.
They can be numbers, small texts or identifier representing a choice for multiple choice questions.
* ``order``: provides an integer value which represents the number of questions asked before that particular question giving the order of the entire questionnaire.
* ``choice_text``: represents the texts in the choices of the multiple choice questions which the users
selected as answers.



MMMBackgroundMeta, MMMBaselineMeta, MMMDiagnosticPatientMeta, MMMFeedbackPostActiveMeta, MMMPostActiveMeta, MMMSurveyAllMeta
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

These 6 tables provide meta data for their respective set of questionnaires’ answers. Each of these tables summerize the overall information gathered per user for that particular set of questionnaire. All of
the data in these 6 tables were collected only once.

* ``name``: the name of the survey.
* ``access_time``: unixtime of the moment when the participant started answering the questions.
* ``seconds``: describes the time (in seconds) it took for the user to provide the answers.
* ``n_questions``: number of questions to be answered in the survey.
