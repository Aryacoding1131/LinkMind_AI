from typing import TypedDict

from langgraph.graph import StateGraph, END

from ai.scraper import scrape_website
from ai.nlp import process_text
from ai.classifier import classify_website
from ai.summarizer import summarize_content

from utils.helpers import get_domain


class BookmarkState(TypedDict):

    url: str

    result: dict

    nlp: dict

    classification: dict

    summary: dict

    bookmark: dict


def scrape_node(state: BookmarkState):

    result = scrape_website(
        state["url"]
    )

    state["result"] = result

    return state

def nlp_node(state):

    result = process_text(
        state["result"]["clean_text"]
    )

    state["nlp"] = result

    return state

def classify_node(state):

    classification = classify_website(
        state["nlp"]["clean_text"]
    )

    if not isinstance(classification, dict):

        classification = {

            "category": "Others",

            "confidence": 0,

            "tags": []

        }

    state["classification"] = classification

    return state

def summary_node(state):

    summary = summarize_content(
        state["nlp"]["clean_text"]
    )

    if not isinstance(summary, dict):

        summary = {

            "summary": "",

            "key_points": [],

            "difficulty": "Unknown",

            "audience": "Unknown"

        }

    state["summary"] = summary

    return state

def build_bookmark_node(state):

    result = state["result"]

    nlp = state["nlp"]

    classification = state["classification"]

    summary = state["summary"]

    state["bookmark"] = {

        "url": state["url"],

        "domain": get_domain(state["url"]),

        "title": result["title"],

        "description": result["description"],

        "content": result["clean_text"],

        "headings": result["headings"],

        "word_count": result["word_count"],

        "clean_text": nlp["clean_text"],

        "keywords": nlp["keywords"],

        "entities": nlp["entities"],

        "reading_time": nlp["reading_time"],

        "category": classification["category"],

        "confidence": classification["confidence"],

        "ai_tags": classification["tags"],

        "summary": summary["summary"],

        "key_points": summary["key_points"],

        "difficulty": summary["difficulty"],

        "audience": summary["audience"]

    }

    return state

graph = StateGraph(BookmarkState)

graph.add_node("scraper", scrape_node)

graph.add_node("nlp", nlp_node)

graph.add_node("classification", classify_node)

graph.add_node("summary", summary_node)

graph.add_node("bookmark", build_bookmark_node)

graph.set_entry_point("scraper")

graph.add_edge("scraper", "nlp")

graph.add_edge("nlp", "classification")

graph.add_edge("classification", "summary")

graph.add_edge("summary", "bookmark")

graph.add_edge("bookmark", END)

workflow = graph.compile()

def run_pipeline(url):

    state = {

        "url": url

    }

    result = workflow.invoke(state)

    return result["bookmark"]
