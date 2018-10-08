package lolplay;

import com.merakianalytics.orianna.Orianna
import com.merakianalytics.orianna.types.core._

import com.merakianalytics.orianna.types.common.Queue
import com.merakianalytics.orianna.types.common.Region
import com.merakianalytics.orianna.types.core.league.League
import com.merakianalytics.orianna.types.core.staticdata.Champion
import com.merakianalytics.orianna.types.core.staticdata.Champions
import com.merakianalytics.orianna.types.core.summoner.Summoner


/**
  * Entry point for our app
  */
object App extends App {
  println("hello world")

  val api_key = "RGAPI-eed927d5-06d3-4eac-b4ac-f243bd421004"

  Orianna.setRiotAPIKey(api_key)
  Orianna.setDefaultRegion(Region.NORTH_AMERICA)


  val summoner: Summoner = Orianna.summonerNamed("FatalElement").get
  System.out.println(summoner.getName + " is level " + summoner.getLevel + " on the " + summoner.getRegion + " server.")

  val champions: Champions = Orianna.getChampions
  val randomChampion: Champion = champions.get((Math.random * champions.size).asInstanceOf[Int])
  System.out.println("He enjoys playing champions such as " + randomChampion.getName)

  val challengerLeague: League = Orianna.challengerLeagueInQueue(Queue.RANKED_SOLO_5x5).get
  val bestNA: Summoner = challengerLeague.get(0).getSummoner
  System.out.println("He's not as good as " + bestNA.getName + " at League, but probably a better Java programmer!")
}