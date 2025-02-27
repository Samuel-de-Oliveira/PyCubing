import requests

__version__: str = '0.1'
__author__: str = 'Samuel de Oliveira'
__license__: str = 'MIT'
__doc__: str = """
-*--------- The PyCubing official docs ---------*-

    Everything can be finded at this link:
    https://github.com/Samuel-de-Oliveira/PyCubing

-*----------------------------------------------*-
"""

__all__: list = [
    'get_wca_rankig',
    'API_MODALITIES',
]

API_MODALITIES: dict = {
    '2x2x2': '222',
    '3x3x3': '333',
    '4x4x4': '444',
    '5x5x5': '555',
    '6x6x6': '666',
    '7x7x7': '777',
    '3x3x3bf': '333bf',
    '3x3x3mbf': '333mbf',
    '3x3x3oh': '333oh',
    '3x3x3ft': '333ft',
    '4x4x4bf': '444bf',
    '5x5x5bf': '555bf',
    'clock': 'clock',
    'megaminx': 'minx',
    'pyraminx': 'pyram',
    'skewb': 'skewb',
    'square_one': 'sq1',
}

# This API is powered by Robin Ingelbrecht at https://github.com/robiningelbrecht/wca-rest-api
WCA_UNOFFICIAL_API: str = 'https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api'


def get_wca_ranking(
    event: str = '3x3x3',
    region: str = 'world',
    score_type: str = 'average',
    rank_size: int = 10,
) -> dict:
    """
    Get the best scores of a WCA modality
    and return it in a dictionary
    """

    get_ranking = requests.get(
        f'{WCA_UNOFFICIAL_API}/rank/{region}/{score_type}/{API_MODALITIES[event]}.json'
    )
    ranking: dict = {}
    for person in range(0, rank_size):
        ranking[get_ranking.json()['items'][person]['personId']] = (
            get_ranking.json()['items'][person]['best'] / 100
        )

    return ranking


if __name__ == '__main__':
    print('This is a module file, then you should import it.')
