from app.services.app import app
from . import algorithm
from . import graphs
from . import gdf


def init_routes():
    app.add_url_rule(
        '/methodOne', view_func=algorithm.Algorithm.as_view('methodOne'))

    app.add_url_rule(
        '/graphs', view_func=graphs.Graphs.as_view('graphs'))

    app.add_url_rule(
        '/gdf', view_func=gdf.Gdf.as_view('gdf'))
