from qgis.core import *
from qgis.utils import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time, json, os

path = 'your repository'

with open(path + '/atributos.json', 'rb') as file:
    atri_dic = json.load(file)

arquivos = os.listdir(path + '/shapefile')
arquivos_shp = [arq for arq in arquivos if arq[-4:] == '.shp']

    
for shp_file in arquivos_shp:

    for elemento in atri_dic.keys():
        QgsProject.instance().clear()
        path_shp = path + '/shapefile/' + shp_file
        vlayer = QgsVectorLayer(path_shp, atri_dic[elemento][6])
        project = QgsProject.instance()
        project.addMapLayer(vlayer)
        layer = iface.activeLayer()
        features = layer.getFeatures()
        

        area_total_shapefile = 0
        area1,area2, area3, area4, area5, area6 = 0,0,0,0,0,0
        
        if elemento not in ['C_Superfic','C_SubSuper','C_Compacta','C_Argila','Class_Fina']:

            for elem in features:
                if elemento in ['P'] and elem['ARGILA'] < 250:
                    primeiro = atri_dic[elemento][0][0]
                    segundo_1, segundo_2 = atri_dic[elemento][1][0], atri_dic[elemento][1][1]
                    terceiro_1, terceiro_2 = atri_dic[elemento][2][0], atri_dic[elemento][2][1]
                    quarto_1, quarto_2 = atri_dic[elemento][3][0], atri_dic[elemento][3][1]
                    quinto_1, quinto_2 = atri_dic[elemento][4][0], atri_dic[elemento][4][1]
                    sexto = atri_dic[elemento][5][0]
                elif elemento in ['P_2'] and elem['ARGILA_1'] < 250:
                    primeiro = atri_dic[elemento][0][0]
                    segundo_1, segundo_2 = atri_dic[elemento][1][0], atri_dic[elemento][1][1]
                    terceiro_1, terceiro_2 = atri_dic[elemento][2][0], atri_dic[elemento][2][1]
                    quarto_1, quarto_2 = atri_dic[elemento][3][0], atri_dic[elemento][3][1]
                    quinto_1, quinto_2 = atri_dic[elemento][4][0], atri_dic[elemento][4][1]
                    sexto = atri_dic[elemento][5][0]
                elif elemento in ['P'] and elem['ARGILA'] >= 250 and elem['ARGILA'] < 400:
                    primeiro = atri_dic[elemento][0][1]
                    segundo_1, segundo_2 = atri_dic[elemento][1][2], atri_dic[elemento][1][3]
                    terceiro_1, terceiro_2 = atri_dic[elemento][2][2], atri_dic[elemento][2][3]
                    quarto_1, quarto_2 = atri_dic[elemento][3][2], atri_dic[elemento][3][3]
                    quinto_1, quinto_2 = atri_dic[elemento][4][2], atri_dic[elemento][4][3]
                    sexto = atri_dic[elemento][5][1]
                elif elemento in ['P_2'] and elem['ARGILA_1'] >= 250 and elem['ARGILA_1'] < 400:
                    primeiro = atri_dic[elemento][0][1]
                    segundo_1, segundo_2 = atri_dic[elemento][1][2], atri_dic[elemento][1][3]
                    terceiro_1, terceiro_2 = atri_dic[elemento][2][2], atri_dic[elemento][2][3]
                    quarto_1, quarto_2 = atri_dic[elemento][3][2], atri_dic[elemento][3][3]
                    quinto_1, quinto_2 = atri_dic[elemento][4][2], atri_dic[elemento][4][3]
                    sexto = atri_dic[elemento][5][1]
                elif elemento in ['P'] and elem['ARGILA'] >=  400:
                    primeiro = atri_dic[elemento][0][2]
                    segundo_1, segundo_2 = atri_dic[elemento][1][4], atri_dic[elemento][1][5]
                    terceiro_1, terceiro_2 = atri_dic[elemento][2][4], atri_dic[elemento][2][5]
                    quarto_1, quarto_2 = atri_dic[elemento][3][4], atri_dic[elemento][3][5]
                    quinto_1, quinto_2 = atri_dic[elemento][4][4], atri_dic[elemento][4][5]
                    sexto = atri_dic[elemento][5][2]
                elif elemento in ['P_2'] and elem['ARGILA_1'] >=  400:
                    primeiro = atri_dic[elemento][0][2]
                    segundo_1, segundo_2 = atri_dic[elemento][1][4], atri_dic[elemento][1][5]
                    terceiro_1, terceiro_2 = atri_dic[elemento][2][4], atri_dic[elemento][2][5]
                    quarto_1, quarto_2 = atri_dic[elemento][3][4], atri_dic[elemento][3][5]
                    quinto_1, quinto_2 = atri_dic[elemento][4][4], atri_dic[elemento][4][5]
                    sexto = atri_dic[elemento][5][2]
                else:
                    primeiro = atri_dic[elemento][0][0]
                    segundo_1, segundo_2 = atri_dic[elemento][1][0], atri_dic[elemento][1][1]
                    terceiro_1, terceiro_2 = atri_dic[elemento][2][0], atri_dic[elemento][2][1]
                    quarto_1, quarto_2 = atri_dic[elemento][3][0], atri_dic[elemento][3][1]
                    quinto_1, quinto_2 = atri_dic[elemento][4][0], atri_dic[elemento][4][1]
                    sexto = atri_dic[elemento][5][0]
                
                if elem[elemento] < primeiro:
                    geom = elem.geometry()
                    area1 = area1 + geom.area()
                elif elem[elemento] >= segundo_1 and elem[elemento] < segundo_2:
                    geom = elem.geometry()
                    area2 = area2 + geom.area()
                elif elem[elemento] >= terceiro_1 and elem[elemento] < terceiro_2:
                    geom = elem.geometry()
                    area3 = area3 + geom.area()
                elif elem[elemento] >= quarto_1 and elem[elemento] < quarto_2:
                    geom = elem.geometry()
                    area4 = area4 + geom.area()
                elif elem[elemento] >= quinto_1 and elem[elemento] < quinto_2:
                    geom = elem.geometry()
                    area5 = area5 + geom.area()
                elif elem[elemento] >= sexto:
                    geom = elem.geometry()
                    area6 = area6 + geom.area()
                    
                geom = elem.geometry()
                print(area_total_shapefile)
                area_total_shapefile = area_total_shapefile + geom.area()
        else:
            for elem in layer.getFeatures():
                if elem[elemento] == atri_dic[elemento][0]:
                    geom = elem.geometry()
                    area1 = area1 + geom.area()
                elif elem[elemento] == atri_dic[elemento][1]:
                    geom = elem.geometry()
                    area2 = area2 + geom.area()
                elif elem[elemento] == atri_dic[elemento][2]:
                    geom = elem.geometry()
                    area3 = area3 + geom.area()
                elif elem[elemento] == atri_dic[elemento][3]:
                    geom = elem.geometry()
                    area4 = area4 + geom.area()
                elif elem[elemento] == atri_dic[elemento][4]:
                    geom = elem.geometry()
                    area5 = area5 + geom.area()
                elif elem[elemento] == atri_dic[elemento][5]:
                    geom = elem.geometry()
                    area6 = area6 + geom.area()

                geom = elem.geometry()
                area_total_shapefile = area_total_shapefile + geom.area()    
        
        
        print(elemento, area_total_shapefile)
            
        if area_total_shapefile == 0:
            continue
            
        area1_porc = round((area1 / area_total_shapefile) * 100,2)
        area2_porc = round((area2 / area_total_shapefile) * 100,2)
        area3_porc = round((area3 / area_total_shapefile) * 100,2)
        area4_porc = round((area4 / area_total_shapefile) * 100,2)
        area5_porc = round((area5 / area_total_shapefile) * 100,2)
        area6_porc = round((area6 / area_total_shapefile) * 100,2)
            



        if elemento in ['AL','AL_2']:
            cores = ['darkGreen','#6ac84b', 'yellow', '#ff681c','red']
        elif elemento in ['ARGILA', 'ARGILA_1']:
            cores = ['#ffffd4', '#fed98e', '#fe9929', '#d95f0e', '#993404', '#5a1e02']
        elif elemento in ['C_Superfic','C_SubSuper','C_Compacta','C_Argila','Class_Fina']:
            cores = ['blue', 'green', 'yellow', '#ff560e', 'red', '#5a1e02']
        elif elemento in  ['PH_CACL2_2', 'PH_CACL2']:
            cores = ['red', 'yellow', '#6ac84b', 'yellow', 'red','darkMagenta']
        elif elemento in  ['CA', 'CA_2','MG','MG_2','K','K_2','S','S_2', 'MOS', 'MO_2']:
            cores = ['red', '#ff560e', 'yellow', '#6ac84b','darkGreen']
        elif elemento in  ['M%','M%_2']:
            cores = ['darkGreen','#6ac84b', 'yellow', '#ff681c','red']
        else:
            cores = ['red','#ff681c', 'yellow','#6ac84b','darkGreen','darkMagenta']




        if elemento in ['AL','CA','MG','M%', 'MOS','MO_2','K','S','AL_2','M%_2','CA_2','MG_2',
                'K_2','S_2','CTC_PH7_2', 'CTC_EFET_1','CTC_PH7','CTC_EFETIV']:
            values_lista = [
                ('(< ' + str(primeiro) + ') - Muito baixo | ' + str(round(area1/10000,2)) + ' ha (' + str(area1_porc) + '%)', 0, primeiro, cores[0]),
                ('(' + str(segundo_1) +' - '+str(segundo_2) + ') - Baixo | ' + str(round(area2/10000,2)) + ' ha (' + str(area2_porc) + '%)', segundo_1, segundo_2, cores[1]),
                ('(' + str(terceiro_1) +' - '+str(terceiro_2) + ') - Médio | ' + str(round(area3/10000,2)) + ' ha (' + str(area3_porc) + '%)', terceiro_1, terceiro_2, cores[2]),
                ('(' + str(quarto_1) +' - '+str(quarto_2) + ') - Alto | ' + str(round(area4/10000,2)) + ' ha (' + str(area4_porc) + '%)', quarto_1, quarto_2, cores[3]),
                ('(> ' + str(quinto_1) + ') - Muito alto | ' + str(round(area5/10000,2)) + ' ha (' + str(area5_porc) + '%)', quinto_1, 100000000000, cores[4])
            ]
        elif elemento in ['ARGILA', 'ARGILA_1']:
            values_lista = [
                ('(< ' + str(primeiro) + ') - Arenoso | ' + str(round(area1/10000,2)) + ' ha (' + str(area1_porc) + '%)', 0, primeiro, cores[0]),
                ('(' + str(segundo_1) +' - '+str(segundo_2) + ') - Textura média | ' + str(round(area2/10000,2)) + ' ha (' + str(area2_porc) + '%)', segundo_1, segundo_2, cores[1]),
                ('(' + str(terceiro_1) +' - '+str(terceiro_2) + ') - Argiloso | ' + str(round(area3/10000,2)) + ' ha (' + str(area3_porc) + '%)', terceiro_1, terceiro_2, cores[2]),
                ('(' + str(quarto_1) +' - '+str(quarto_2) + ') - Muito argiloso | ' + str(round(area4/10000,2)) + ' ha (' + str(area4_porc) + '%)', quarto_1, quarto_2, cores[3]),
                ('(> ' + str(quinto_1) + ') - Muito argiloso | ' + str(round(area5/10000,2)) + ' ha (' + str(area5_porc) + '%)', quinto_1, 100000000000, cores[4])
            ]
        elif elemento in ['C_Superfic','C_SubSuper','C_Compacta','C_Argila','Class_Fina']:
            values_lista = [
                    ('(< ' + str(atri_dic[elemento][0]) + ') - Muito baixo | ' + str(round(area1/10000,2)) + ' ha (' + str(area1_porc) + '%)', atri_dic[elemento][0], cores[0]),
                    ('(' + str(atri_dic[elemento][1]) + ') - Baixo | ' + str(round(area2/10000,2)) + ' ha (' + str(area2_porc) + '%)', atri_dic[elemento][1], cores[1]),
                    ('(' + str(atri_dic[elemento][2]) + ') - Médio | ' + str(round(area3/10000,2)) + ' ha (' + str(area3_porc) + '%)', atri_dic[elemento][2], cores[2]),
                    ('(' + str(atri_dic[elemento][3]) + ') - Alto | ' + str(round(area4/10000,2)) + ' ha (' + str(area4_porc) + '%)', atri_dic[elemento][3], cores[3]),
                    ('(' + str(atri_dic[elemento][4]) + ') - Muito alto | ' + str(round(area5/10000,2)) + ' ha (' + str(area5_porc) + '%)', atri_dic[elemento][4], cores[4]),
                    ('(> ' + str(atri_dic[elemento][5]) + ') - Condições a evitar | ' + str(round(area6/10000,2)) + ' ha (' + str(area6_porc) + '%)', atri_dic[elemento][5][0], cores[5])
            ]        
        else:
            values_lista = [
                ('(' + str(primeiro) + ') - Muito baixo | ' + str(round(area1/10000,2)) + ' ha (' + str(area1_porc) + '%)', 0, primeiro, cores[0]),
                ('(' + str(segundo_1) +' - '+str(segundo_2) + ') - Baixo | ' + str(round(area2/10000,2)) + ' ha (' + str(area2_porc) + '%)', segundo_1, segundo_2, cores[1]),
                ('(' + str(terceiro_1) +' - '+str(terceiro_2) + ') - Médio | ' + str(round(area3/10000,2)) + ' ha (' + str(area3_porc) + '%)', terceiro_1, terceiro_2, cores[2]),
                ('(' + str(quarto_1) +' - '+str(quarto_2) + ') - Alto | ' + str(round(area4/10000,2)) + ' ha (' + str(area4_porc) + '%)', quarto_1, quarto_2, cores[3]),
                ('(' + str(quinto_1) +' - '+str(quinto_2) + ') - Muito alto | ' + str(round(area5/10000,2)) + ' ha (' + str(area5_porc) + '%)', quinto_1, quinto_2, cores[4]),
                ('(' + str(sexto) +') - Condições a evitar | ' + str(round(area6/10000,2)) + ' ha (' + str(area6_porc) + '%)', sexto, 100000000000, cores[5])
            ]
        
        values = []
        for item in values_lista:
            if '0 ha' in item[0]:
                pass
            else:
                values.append(item)
                
        if elemento not in ['C_Superfic','C_SubSuper','C_Compacta','C_Argila','Class_Fina']:    
            ranges = []
            for label, lower, upper, color in values:
                try:
                    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
                    symbol.setColor(QColor(color))
                    rng = QgsRendererRange(lower, upper, symbol, label)
                    ranges.append(rng)
                except:
                    pass
            expression = elemento
            renderer = QgsGraduatedSymbolRenderer(expression, ranges)
        else:
            ranges = []
            for label, value, color in values:
                try:
                    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
                    symbol.setColor(QColor(color))
                    rng = QgsRendererCategory(value, symbol, label)
                    ranges.append(rng)
                except:
                    pass
            expression = elemento
            renderer = QgsCategorizedSymbolRenderer(expression, ranges)
                
        layer.setRenderer(renderer)
        layer.triggerRepaint()
            
        if elemento in ['CTC_EFET_1','CTC_PH7_2','CTC_PH7','CTC_EFETIV']:
            pass
        else:
            layer_settings  = QgsPalLayerSettings()
            text_format = QgsTextFormat()
            text_format.setFont(QFont("Arial", 10))
            text_format.setSize(10)
            buffer_settings = QgsTextBufferSettings()
            buffer_settings.setEnabled(False)
            buffer_settings.setSize(0.1)
            buffer_settings.setColor(QColor("black"))
            text_format.setBuffer(buffer_settings)
            layer_settings.setFormat(text_format)
            layer_settings.fieldName = elemento
            layer_settings.placement = 0
            layer_settings.enabled = True
            layer_settings = QgsVectorLayerSimpleLabeling(layer_settings)
            layer.setLabelsEnabled(True)
            layer.setLabeling(layer_settings)
            layer.triggerRepaint()



        manager = project.layoutManager()
        layoutName = 'Layout1'
        layout = QgsPrintLayout(project)
        layout.initializeDefaults()
        layout.setName(layoutName)
        manager.addLayout(layout)



        map = QgsLayoutItemMap(layout)
        map.setRect(30, 30, 30, 30)
        ms = QgsMapSettings()
        ms.setLayers([layer])
        rect = QgsRectangle(ms.fullExtent())
        rect.scale(1.2)
        ms.setExtent(rect)
        map.setExtent(rect)
        map.setBackgroundColor(QColor(255, 255, 255, 0))
        map.attemptMove(QgsLayoutPoint(10, 10, QgsUnitTypes.LayoutMillimeters))
        
        #Alterar escala
        map.attemptResize(QgsLayoutSize(250, 250, QgsUnitTypes.LayoutMillimeters))
#        map.setExtent(ms.fullExtent())
        layout.addLayoutItem(map)



        legend = QgsLayoutItemLegend(layout)
        layerTree = QgsLayerTree()
        layerTree.addLayer(layer)
        legend.model().setRootGroup(layerTree)
        layout.addLayoutItem(legend)
        legend.attemptMove(QgsLayoutPoint(180, 15, QgsUnitTypes.LayoutMillimeters))

        layout = manager.layoutByName(layoutName)
        exporter = QgsLayoutExporter(layout)
        time.sleep(3)

        finalFile = path + '/images/' + shp_file + '_' + elemento + ".png"
        exporter.exportToImage(finalFile, QgsLayoutExporter.ImageExportSettings())
        

