
public interface PixelMathAbstractionInterface{
    public int  getPixelQuickly(int id, float x, float y);
    public void setPixelQuickly(int id, float x, float y, int color);

    public void openImage(int id, String filename);
    public int  newImage(int id, String title, int width, int height,
                         int r, int g, int b);

    public int getImageWidth(int id);
    public int getImageHeight(int id);

    public void refresh(int id);
}
