# your_app/management/commands/seed.py
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from items.models import Product
import random

class Command(BaseCommand):
    help = 'Seed the database with Hasui Kawase paintings'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        paintings = [
            {
                "name": "Zōjō-ji Temple in Shiba",
                "description": "Whispers of history at dawn, where shadows dance and morning awakens.",
                "picture_url": "https://www.artic.edu/iiif/2/1e649de9-30b6-7bc9-3f1d-636508c223ad/full/843,/0/default.jpg",
                "full_description": "A stunning portrayal of Zōjō-ji Temple, capturing the serene atmosphere of early morning. The intricate details and masterful use of light and shadow bring this historic site to life, evoking a sense of tranquility and timelessness."
            },
            {
                "name": "Snow at Ueno Kiyomizudō",
                "description": "Silent snowflakes in twilight, a winter's hush envelops the scene.",
                "picture_url": "https://moonlitseaprints.com/wp-content/uploads/2022/06/kawase-hasui-snow-at-ueno-kiyomizudo-scaled.jpg",
                "full_description": "An evocative winter scene at Ueno Kiyomizudō, showcasing the tranquil beauty of snow-covered landscapes. The serene atmosphere invites viewers into a peaceful, almost meditative state, where the gentle snowfall creates a blanket of quietude."
            },
            {
                "name": "Spring Moon at Ninomiya Beach",
                "description": "Mystery under the moon, where night's whispers carry ancient tales.",
                "picture_url": "https://i0.wp.com/www.themarginalian.org/wp-content/uploads/2021/03/hasuikawase1.jpg?w=1200&ssl=1",
                "full_description": "A mesmerizing night view of Hakone, highlighting the mystical allure of the area under moonlight. The careful attention to natural and architectural elements creates a scene filled with quiet wonder and an air of enchantment."
            },
            {
                "name": "Evening at Itako",
                "description": "Soft hues of dusk, painting the sky in gentle whispers of color.",
                "picture_url": "https://i0.wp.com/nipponprints.com/wp-content/uploads/2023/09/japanese-woodblock-print-kawase-hasui-evening-at-itako-scaled.jpg?fit=1200%2C1654&ssl=1",
                "full_description": "A gentle portrayal of evening at Itako, emphasizing the soft, warm colors of dusk. The calm ambiance of the town as day transitions to night is beautifully captured, creating a sense of serenity and reflective peace."
            },
            {
                "name": "Rain at Shinagawa",
                "description": "Raindrops dance on streets, weaving a tapestry of motion and stillness.",
                "picture_url": "https://moonlitseaprints.com/wp-content/uploads/2021/01/kawase-hasui-rain-at-shinagawa-featured.jpg",
                "full_description": "A vivid depiction of a rainy day at Shinagawa, where the artist skillfully captures the dynamic interaction between rain and urban life. The scene is brought to life with a sense of movement and fluidity, reflecting the vibrant energy of the city."
            },
            {
                "name": "Moon over Magome",
                "description": "Moonlit whispers of nature, where silence speaks volumes.",
                "picture_url": "https://www.roningallery.com/Inventory_Images/JPR-109926_Main-1.jpg?resizeid=5&resizeh=1800&resizew=1800",
                "full_description": "An enchanting scene of Magome under moonlight, illustrating the serene and mystical atmosphere of the area. The focus on natural beauty and tranquil moments invites viewers into a world of quiet reflection and gentle wonder."
            },
            {
                "name": "Spring Night at Inokashira Park",
                "description": "Spring blooms in twilight, where nature's beauty unfolds softly.",
                "picture_url": "https://www.roningallery.com/Inventory_Images/JP-208433_Main-01?resizeid=5&resizeh=1800&resizew=1800",
                "full_description": "A delightful representation of a spring evening at Inokashira Park, featuring blooming flowers and the park's peaceful environment. As day turns to night, the scene captures the delicate balance of light and shadow, bringing a sense of renewal and calm."
            },
            {
                "name": "Snow at Mukojima",
                "description": "Snowy silence prevails, cloaking the world in a pristine embrace.",
                "picture_url": "https://www.roningallery.com/Inventory_Images/JPR1-58377_Main-1.jpg?resizeid=5&resizeh=1800&resizew=1800",
                "full_description": "A tranquil winter scene at Mukojima, where the artist captures the quiet and serene beauty of snow-covered landscapes. The gentle snowfall and peaceful surroundings evoke a sense of calm and introspection, offering a moment of pure tranquility."
            },
            {
                "name": "Dusk at Asao",
                "description": "Twilight tales of old, where history and light intertwine.",
                "picture_url": "https://i.etsystatic.com/15063307/r/il/e62789/2706209942/il_1588xN.2706209942_hfo5.jpg",
                "full_description": "A captivating depiction of dusk at Asakusa, focusing on the rich cultural and historical elements of the area. Bathed in the soft, fading light of evening, the scene creates a bridge between the past and present, filled with nostalgic beauty."
            },
            {
                "name": "Matsushima in the Moonlight",
                "description": "Moonlit reflections dance, where water mirrors the sky's glow.",
                "picture_url": "https://www.artic.edu/iiif/2/ecfa9d50-cc97-3391-303a-7dbf757630bc/full/843,/0/default.jpg",
                "full_description": "A serene portrayal of Matsushima under moonlight, highlighting the tranquil and reflective nature of the area. The interplay between water and moonlight creates a scene of ethereal beauty, inviting viewers to experience the calm and quiet majesty of the night."
            }
        ]

        try:
            with transaction.atomic():
                for painting in paintings:
                    Product.objects.create(
                        name=painting["name"],
                        description=painting["description"],
                        full_description=painting["full_description"],
                        picture_url=painting["picture_url"],
                        price=random.uniform(10000000.0, 50000000.0)
                    )
            self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))
        except Exception as e:
            raise CommandError(f'Error seeding database: {e}')