#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import requests
from fake_useragent import UserAgent
import json

headers = {
    'User-Agent': UserAgent()
}