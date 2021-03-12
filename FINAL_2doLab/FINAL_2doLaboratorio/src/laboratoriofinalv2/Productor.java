/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package laboratoriofinalv2;

/**
 *
 * @author estudiante.fit
 */
public class Productor extends Thread{
    
    private int garrafas = 2400;
    private Planta planta;
    private String id;

    public Productor( Planta planta, String id) {
        this.planta = planta;
        this.id = id;
    }
    
    @Override
    public void run(){
        while (true){
            planta.producirGarrafas();
        }
    
    }
    
    
}
