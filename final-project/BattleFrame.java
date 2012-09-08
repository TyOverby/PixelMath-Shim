import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;


public class BattleFrame extends JFrame {
	private static final long serialVersionUID = -536170179835589769L;
	
	private JPanel contentPane;
	private final boolean whichTeam;
	private final Color[] team1Colors; 
	private final Color[] team2Colors;
	
	private final List<JButton> team1Buttons = new ArrayList<JButton>();
	private final List<JButton> team2Buttons = new ArrayList<JButton>();
	
	public boolean isFinished = false;
	
	public Color team1Chosen;
	public Color team2Chosen;
	private JPanel displayPanel;
	private JPanel opposerPanel;
	private JButton btnDone;

	/**
	 * Create the frame.
	 */
	private BattleFrame(boolean whichTeam, Color[] team1Colors, Color[] team2Colors) {
		this.whichTeam = whichTeam;
		this.team1Colors = team1Colors;
		this.team2Colors = team2Colors;
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		String lll = whichTeam? "1": "2";
		JLabel lblTeamPicks = new JLabel("Team "+lll+" Picks First");
		lblTeamPicks.setBounds(134, 12, 156, 15);
		contentPane.add(lblTeamPicks);
		
		JLabel lblTeam = new JLabel("Team 1");
		lblTeam.setBounds(21, 40, 70, 15);
		contentPane.add(lblTeam);
		
		JLabel lblTeam_1 = new JLabel("Team 2");
		lblTeam_1.setBounds(376, 40, 70, 15);
		contentPane.add(lblTeam_1);
		
		displayPanel = new JPanel();
		displayPanel.setBackground(new Color(0, 0, 0));
		displayPanel.setBounds(153, 53, 140, 136);
		contentPane.add(displayPanel);
		displayPanel.setLayout(null);
		
		opposerPanel = new JPanel();
		opposerPanel.setBounds(20, 20, 50, 50);
		displayPanel.add(opposerPanel);
		opposerPanel.setBackground(new Color(255, 255, 255));
		
		btnDone = new JButton("Done");
		btnDone.setEnabled(false);
		btnDone.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				BattleFrame.this.isFinished = true;
			}
		});
		btnDone.setBounds(163, 201, 117, 25);
		contentPane.add(btnDone);
		
		int count1 = 0;
		for(Color color:this.team1Colors){
			final JButton button = new JButton("");
			team1Buttons.add(button);
			button.setBounds(20,60+25*count1,100,20);
			button.setBackground(color);
			contentPane.add(button);
			if(!this.whichTeam){
				button.setEnabled(false);
			}
			button.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent e) {
					BattleFrame.this.team1Chosen = button.getBackground();
					if(BattleFrame.this.whichTeam){
						displayPanel.setBackground(button.getBackground());
						for(JButton b:team1Buttons){
							b.setEnabled(false);
						}
						for(JButton b:team2Buttons){
							b.setEnabled(true);
						}
					}
					else{
						opposerPanel.setBackground(button.getBackground());
						btnDone.setEnabled(true);
					}
				}
			});
			count1++;
		}
		
		int count2 = 0;
		for(Color color:this.team2Colors){
			final JButton button = new JButton("");
			team2Buttons.add(button);
			button.setBounds(450-20-100,60+25*count2,100,20);
			button.setBackground(color);
			contentPane.add(button);
			if(this.whichTeam){
				button.setEnabled(false);
			}
			button.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent e) {
					BattleFrame.this.team2Chosen = button.getBackground();
					if(!BattleFrame.this.whichTeam){
						displayPanel.setBackground(button.getBackground());
						for(JButton b:team2Buttons){
							b.setEnabled(false);
						}
						for(JButton b:team1Buttons){
							b.setEnabled(true);
						}
					}
					else{
						opposerPanel.setBackground(button.getBackground());
						btnDone.setEnabled(true);
					}
				}
			});
			count2++;
		}
		
	}
	
	private Color[] getChosen(){
		Color[] toReturn = new Color[2];
		toReturn[0] = team1Chosen;
		toReturn[1] = team2Chosen;
		
		return toReturn;
	}
	
	public static Color[] getResults(boolean whichTeam, Color[] team1Colors, Color[] team2Colors){
		BattleFrame frame = new BattleFrame(whichTeam, team1Colors, team2Colors);
		frame.setVisible(true);
		
		while(!frame.isFinished){
			try {
				Thread.sleep(100);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		frame.dispose();
		return frame.getChosen();
	}
	
	
	public static Color randColor(){
		Random rand = new Random();
		return new Color(rand.nextInt(256),rand.nextInt(256),rand.nextInt(256));
	}
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		boolean which = true;
		
		Color[] team1 = new Color[6];
		Color[] team2 = new Color[6];
		
		for(int i=0;i<team1.length;i++){
			team1[i] = randColor();
			team2[i] = randColor();
		}
		
		for(Color c: BattleFrame.getResults(which, team1, team2)){
			System.out.println(c.toString());
		}
	}
}
