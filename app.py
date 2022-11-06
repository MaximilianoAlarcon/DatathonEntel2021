from yolo.model import Model
import time

def main():
    start_time = time.time()

    print("Iniciando detección de firmas y campos de fecha con el modelo Yolo-SDF...")
    sdf = Model()
    sdf.excecute_sdf()
    print("Yolo-SDF ha terminado exitosamente.")
    print("Iniciando detección de números y formateando las fechas con el modelo Yolo-DOCR...")
    sdf.execute_docr(partial='1502.weights')
    print("Yolo-DOCR ha terminado exitosamente.")
    print("El modelo ha corrido exitosamente. Dirígete a la carpeta /output para ver las salidas del modelo.")
    print("Se realizó la detección de firmas y fechas de las 107 imágenes de prueba en "+str(time.time() - start_time)+" segundos")

if __name__ == "__main__":
    main()
