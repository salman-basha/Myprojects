import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class Login extends JFrame
{
	public static void main (String s[])
	{
		JFrame frame = new JFrame ("Login Page");
		frame.setLayout(new GridLayout(3,2));
		JLabel l1 = new JLabel ("Enter Your UserName:-");
		JTextField t1 = new JTextField();
		JLabel l2 = new JLabel ("Enter Your Password:-");
		JPasswordField p1 = new JPasswordField();
		JButton b1= new JButton();
		b1.setText("Login");
		b1.addActionListener(new ActionListener()
		{
			public void actionPerformed(ActionEvent e)
			{
				new StudentDetails();
				b1.setText("Login Successfully!");
			}
		});
		JButton b2= new JButton();
		b2.setText("Exit");
		b2.addActionListener(new ActionListener()
		{
			public void actionPerformed(ActionEvent e)
			{
				System.exit(0);
			}
		});
		frame.add(l1);
		frame.add(t1);
		frame.add(l2);
		frame.add(p1);
		frame.add(b1);
		frame.add(b2);
		
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(250,300);
		frame.setVisible(true);
	}
}