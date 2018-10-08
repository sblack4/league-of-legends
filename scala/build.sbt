
name := "lol-play"
organization := "com.github.sblack4"
version := "0.01"
scalaVersion := "2.11.8"

val sparkVersion = "2.1.0"


resolvers ++= Seq(
  "apache-snapshots" at "http://repository.apache.org/snapshots/"
)


libraryDependencies ++= Seq(
//  "org.apache.spark" %% "spark-core" % sparkVersion,
//  "org.apache.spark" %% "spark-sql" % sparkVersion,
//  "org.apache.spark" %% "spark-hive" % sparkVersion,
//  "log4j" % "log4j" % "1.2.17",
  "com.merakianalytics.orianna" % "orianna" % "3.0.4"
)