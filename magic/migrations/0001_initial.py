# Generated by Django 2.2.1 on 2019-05-12 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(default=0, max_length=120)),
                ('Image', models.TextField(default=0, max_length=120)),
                ('nom', models.TextField(default=0, max_length=120)),
                ('nomFR', models.TextField(default=0, max_length=120)),
                ('nomUS', models.TextField(default=0, max_length=120)),
                ('nomDossier', models.TextField(default=0, max_length=120)),
                ('NbExtensions', models.IntegerField(default=0)),
                ('annee', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'serie',
            },
        ),
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idPCA', models.TextField(default=0, max_length=120)),
                ('name', models.TextField(default=0, max_length=120)),
                ('nom', models.TextField(default=0, max_length=120)),
                ('nomFR', models.TextField(default=0, max_length=120)),
                ('nomUS', models.TextField(default=0, max_length=120)),
                ('nomDossier', models.TextField(default=0, max_length=120)),
                ('dateSortie', models.DateField(default=0)),
                ('nomRaccourci', models.TextField(default=0, max_length=120)),
                ('nbCartes', models.IntegerField(default=0)),
                ('baseSetSize', models.IntegerField(default=0)),
                ('block', models.TextField(default=0, max_length=120)),
                ('boosterV3', models.TextField(default=0, max_length=120)),
                ('code', models.TextField(default=0, max_length=120)),
                ('codeV3', models.TextField(default=0, max_length=120)),
                ('isFoilOnly', models.IntegerField(default=0)),
                ('isOnlineOnly', models.IntegerField(default=0)),
                ('keyruneCode', models.TextField(default=0, max_length=120)),
                ('mcmName', models.TextField(default=0, max_length=120)),
                ('mcmId', models.IntegerField(default=0)),
                ('meta', models.TextField(default=0, max_length=120)),
                ('mtgoCode', models.TextField(default=0, max_length=120)),
                ('parentCode', models.TextField(default=0, max_length=120)),
                ('releaseDate', models.TextField(default=0, max_length=120)),
                ('tcgplayerGroupId', models.IntegerField(default=0)),
                ('totalSetSize', models.IntegerField(default=0)),
                ('type', models.TextField(default=0, max_length=120)),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magic.Serie')),
            ],
            options={
                'db_table': 'extension',
            },
        ),
        migrations.CreateModel(
            name='Carte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idPrim', models.TextField(default=0, max_length=120)),
                ('name', models.TextField(default=0, max_length=120)),
                ('nameFR', models.TextField(default=0, max_length=120)),
                ('nameUS', models.TextField(default=0, max_length=120)),
                ('num', models.TextField(default=0, max_length=120)),
                ('sur', models.TextField(default=0, max_length=120)),
                ('recherche', models.TextField(default=0, max_length=120)),
                ('nomComplet', models.TextField(default=0, max_length=120)),
                ('nomFrancaisEBAY', models.TextField(default=0, max_length=120)),
                ('nomAnglaisEBAY', models.TextField(default=0, max_length=120)),
                ('nomJapEBAY', models.TextField(default=0, max_length=120)),
                ('nomFrancaisZEBRA', models.TextField(default=0, max_length=120)),
                ('nomAllemandZEBRA', models.TextField(default=0, max_length=120)),
                ('nomItalienZEBRA', models.TextField(default=0, max_length=120)),
                ('nomEspagnolZEBRA', models.TextField(default=0, max_length=120)),
                ('nomRusseZEBRA', models.TextField(default=0, max_length=120)),
                ('nomPortugaisZEBRA', models.TextField(default=0, max_length=120)),
                ('nomJapZEBRA', models.TextField(default=0, max_length=120)),
                ('nomAnglaisZEBRA', models.TextField(default=0, max_length=120)),
                ('nomCompletFR', models.TextField(default=0, max_length=120)),
                ('nomCompletUS', models.TextField(default=0, max_length=120)),
                ('nomCompletJAP', models.TextField(default=0, max_length=120)),
                ('table', models.TextField(default=0, max_length=120)),
                ('FR', models.BooleanField(default=0)),
                ('US', models.BooleanField(default=0)),
                ('artist', models.TextField(default=0)),
                ('borderColor', models.TextField(default=0)),
                ('colorIdentity', models.TextField(default=0)),
                ('colorIndicator', models.TextField(default=0)),
                ('colors', models.TextField(default=0)),
                ('convertedManaCost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('duelDeck', models.TextField(default=0)),
                ('faceConvertedManaCost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('flavorText', models.TextField(default=0)),
                ('frameEffect', models.TextField(default=0)),
                ('frameVersion', models.TextField(default=0)),
                ('hand', models.TextField(default=0)),
                ('hasFoil', models.BooleanField(default=0)),
                ('hasNonFoil', models.BooleanField(default=0)),
                ('isAlternative', models.BooleanField(default=0)),
                ('isOnlineOnly', models.BooleanField(default=0)),
                ('isOversized', models.BooleanField(default=0)),
                ('isReserved', models.BooleanField(default=0)),
                ('isStarter', models.BooleanField(default=0)),
                ('isTimeshifted', models.BooleanField(default=0)),
                ('layout', models.TextField(default=0)),
                ('loyalty', models.TextField(default=0)),
                ('manaCost', models.TextField(default=0)),
                ('mcmName', models.TextField(default=0)),
                ('mcmId', models.IntegerField(default=0)),
                ('mcmMetaId', models.IntegerField(default=0)),
                ('mtgstocksId', models.IntegerField(default=0)),
                ('multiverseId', models.IntegerField(default=0)),
                ('names', models.TextField(default=0)),
                ('number', models.TextField(default=0)),
                ('originalText', models.TextField(default=0)),
                ('originalType', models.TextField(default=0)),
                ('printings', models.TextField(default=0)),
                ('prices', models.TextField(default=0)),
                ('power', models.TextField(default=0)),
                ('purchaseUrls', models.TextField(default=0)),
                ('rarity', models.TextField(default=0)),
                ('scryfallId', models.TextField(default=0)),
                ('scryfallOracleId', models.TextField(default=0)),
                ('scryfallIllustrationId', models.TextField(default=0)),
                ('setCode', models.TextField(default=0)),
                ('side', models.TextField(default=0)),
                ('subtypes', models.TextField(default=0)),
                ('supertypes', models.TextField(default=0)),
                ('tcgplayerProductId', models.IntegerField(default=0)),
                ('tcgplayerPurchaseUrl', models.TextField(default=0)),
                ('text', models.TextField(default=0)),
                ('toughness', models.TextField(default=0)),
                ('type', models.TextField(default=0)),
                ('types', models.TextField(default=0)),
                ('uuid', models.CharField(default=0, max_length=36)),
                ('uuidV421', models.TextField(default=0)),
                ('variations', models.TextField(default=0)),
                ('watermark', models.TextField(default=0)),
                ('extension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magic.Extension')),
            ],
            options={
                'db_table': 'carte',
            },
        ),
    ]
