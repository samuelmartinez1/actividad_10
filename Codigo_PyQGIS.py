import processing 
data2 = "C:/Users/Usuario/Desktop/Desarrollo_SIG/Shp_PYqgis/Capas_Actividad_10/Red_Hidrica_HN.shp"
nombre_shp = "Rios_Honduras"
consulta1 = "Codigo = 1"
consulta2 = "Codigo = 2"
consulta3 = "Codigo = 3"
def entrada_rios(entrada,nombre,consulta):
    entrada = entrada
    nombre = nombre
    consulta = consulta
    shp = iface.addVectorLayer(entrada,nombre,"ogr")
    shp.setSubsetString(consulta) 
    return shp 
Capa_rios = entrada_rios(data2 ,nombre_shp ,consulta1) 
capa_rios2 = entrada_rios(data2 ,nombre_shp ,consulta2)
capa_rios3 = entrada_rios(data2 ,nombre_shp ,consulta3) 
#funcion para departamentos 
data = "C:/Users/Usuario/Desktop/Desarrollo_SIG/Shp_PYqgis/Capas_Actividad_10/Limite_Departamental_HN.shp"
nombre = "Dept_Honduras" 
consulta_la_paz = "DEPTO  = 'La Paz' " 
Capa_LaPaz = entrada_rios(data,nombre,consulta_la_paz)
print("capa rios primarios")
layer_clip1 = processing.run('native:clip',{'INPUT':Capa_rios,'OVERLAY':Capa_LaPaz ,'OUTPUT': "C:/Users/Usuario/Desktop/Desarrollo_SIG/Shp_PYqgis/Capas_Actividad_10/Rios_primarios.shp"}) 
print("capa rios secundarios")
layer_clip2 = processing.run('native:clip',{'INPUT':capa_rios2,'OVERLAY':Capa_LaPaz ,'OUTPUT':"C:/Users/Usuario/Desktop/Desarrollo_SIG/Shp_PYqgis/Capas_Actividad_10/Rios_secundarios.shp"}) 
print("capa rios terciarios")
layer_clip3 = processing.run('native:clip',{'INPUT':capa_rios3 ,'OVERLAY':Capa_LaPaz ,'OUTPUT':"C:/Users/Usuario/Desktop/Desarrollo_SIG/Shp_PYqgis/Capas_Actividad_10/Rios_terciarios.shp"}) 
print("buffer capas rios primarios")
#variables 
data3 = "C:/Users/Usuario/Desktop/Desarrollo_SIG/Shp_PYqgis/Capas_Actividad_10/Rios_primarios.shp"
data4 = "C:/Users/Usuario/Desktop/Desarrollo_SIG/Shp_PYqgis/Capas_Actividad_10/Rios_secundarios.shp"
data5 = "C:/Users/Usuario/Desktop/Desarrollo_SIG/Shp_PYqgis/Capas_Actividad_10/Rios_terciarios.shp" 
primario = iface.addVectorLayer(data3,"Rios_primarios","ogr")
secundario = iface.addVectorLayer(data4 ,"Rios_secundarios","ogr")
terciario = iface.addVectorLayer(data5,"Rios_terciarios","ogr")
print("Proceso de buffer primerio")
processing.runAndLoadResults("native:buffer",{'INPUT':primario,'DISTANCE':100,'SEGMENTS':5,'END_CAP_STYLE':0,'JOIN_STYLE':0,'MILTER_LIMIT':2,'DISSOLVE':False,'OUTPUT':"C:/Users/Usuario/Desktop/Desarrollo_SIG/Shp_PYqgis/Capas_Actividad_10/Rios_buffer1.shp"})
print("Proceso de buffer secundario")
processing.runAndLoadResults("native:buffer",{'INPUT':secundario,'DISTANCE':50,'SEGMENTS':5,'END_CAP_STYLE':0,'JOIN_STYLE':0,'MILTER_LIMIT':2,'DISSOLVE':False,'OUTPUT':"C:/Users/Usuario/Desktop/Desarrollo_SIG/Shp_PYqgis/Capas_Actividad_10/Rios_buffer2.shp"})
processing.runAndLoadResults("native:buffer",{'INPUT':terciario,'DISTANCE':20,'SEGMENTS':5,'END_CAP_STYLE':0,'JOIN_STYLE':0,'MILTER_LIMIT':2,'DISSOLVE':False,'OUTPUT':"C:/Users/Usuario/Desktop/Desarrollo_SIG/Shp_PYqgis/Capas_Actividad_10/Rios_buffer3.shp"})