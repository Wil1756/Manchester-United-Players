#!/usr/bin/env python
# encoding: utf-8
import json
import flask
from flask import request, Response, json
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

players = { "players":[ 
                {
                    "name": "David De Gea",
                    "team": "Man United",
                    "goals": 0,
                    "assists": 0,
                    "image": "https://assets.manutd.com/AssetPicker/images/0/0/16/129/1081699/Legends_Profile_DeGea1649253564473.jpg"
                },
                {
                    "name": "Diogo Dalot",
                    "team": "Man United",
                    "goals": 7,
                    "assists": 11,
                    "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fmobile.twitter.com%2Fdalotdiogo&psig=AOvVaw39BTl0OzHeEzDjT9mRDQYw&ust=1666887743986000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCOiahPCm_voCFQAAAAAdAAAAABAE"
                },
                {
                    "name": "Lisandro Matinez",
                    "team": "Man United",
                    "goals": 2,
                    "assists": 1,
                    "image": "https://paininthearsenal.com/wp-content/uploads/getty-images/2017/07/1413493620.jpeg"
                },
                
                {
                    "name": "Raphael Varane",
                    "team": "Man United",
                    "goals": 7,
                    "assists": 0,
                    "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.si.com%2Fsoccer%2Fmanchesterunited%2Fnews%2Fraphael-varane-out-until-world-cup-with-injury&psig=AOvVaw37KrPjIU3wdFNZTQc43rGD&ust=1666887823663000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCIjl1Jan_voCFQAAAAAdAAAAABAE"
                },
                
                {
                    "name": "Luke Shaw",
                    "team": "Man United",
                    "goals": 3,
                    "assists": 2,
                    "image": "https://weallfollowunited.com/wp-content/uploads/2022/10/manchester-city-v-manchester-united-premier-league-1-scaled.jpg"
                },
                {
                    "name": "Scott McTominay",
                    "team": "Man United",
                    "goals": 7,
                    "assists": 4,
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXOb8a6F-m_7XfQ4x6CmX6ekz-ls8B_ZL10A&usqp=CAU"
                },
                {
                    "name": "Casemiro",
                    "team": "Man United",
                    "goals": 27,
                    "assists": 13,
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXOb8a6F-m_7XfQ4x6CmX6ekz-ls8B_ZL10A&usqp=CAU"
                },
                {
                    "name": "Christian Eriksen",
                    "team": "Man United",
                    "goals": 8,
                    "assists": 19,
                    "image": "data:image/jpeg;base64,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"
                },
                {
                    "name": "Bruno Fernandez",
                    "team": "Man United",
                    "goals": 29,
                    "assists": 28,
                    "image": "https://images2.minutemediacdn.com/image/upload/c_crop,w_4207,h_2366,x_0,y_118/c_fill,w_720,ar_16:9,f_auto,q_auto,g_auto/images/GettyImages/mmsport/90min_en_international_web/01g7d2s90nfhqfp7dmp4.jpg"
                },
                {
                    "name": "Markus Rashford",
                    "team": "Man United",
                    "goals": 17,
                    "assists": 21,
                    "image": "https://images.teamtalk.com/content/uploads/2022/10/03151044/marcus-rashford-man-utd-2022.jpg"
                },
                {
                    "name": "Ronaldo",
                    "team": "Man United",
                    "goals": 21,
                    "assists": 33,
                    "image": "https://e0.365dm.com/22/10/768x432/skysports-ronaldo-man-utd_5936635.jpg"
                }
                ]
            }


@app.route('/', methods=["GET", "POST"])
def index():
    return json.dumps(players)

app.run(port=4000)